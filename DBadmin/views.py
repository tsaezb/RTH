from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Comuna, Hospital, Paciente, Habito, Enfermedad
from django.core import serializers
import json

# Create your views here.

@login_required
def userdata(request):
    to_json = {
        "email": request.user.email,
        "username": request.user.username,
        "firstname": request.user.first_name,
        "lastname": request.user.last_name
    }
    return JsonResponse(to_json)

@login_required
def comunas(request):
    resultset = Comuna.objects.all()
    results = [ob.as_json() for ob in resultset]
    return JsonResponse(results, safe=False)

@login_required
def hospitales(request):
    resultset = Hospital.objects.all()
    results = [ob.as_json() for ob in resultset]
    return JsonResponse(results, safe=False)

@login_required
def gruposSanguineos(request):
    data = [{'id': sang[0], 'grupo': sang[1]} for sang in Paciente.op_grupo_sang]
    return JsonResponse(data, safe=False)

@login_required
def previsiones(request):
    data = [{'id': prev[0], 'prevision': prev[1]} for prev in Paciente.op_prevision]
    return JsonResponse(data, safe=False)

@login_required
def habitos(request):
    resultset = Habito.objects.all()
    results = [ob.as_json() for ob in resultset]
    return JsonResponse(results, safe=False)

@login_required
def enfermedades(request):
    resultset = Enfermedad.objects.all()
    results = [ob.as_json() for ob in resultset]
    return JsonResponse(results, safe=False)

@login_required
def pacientesLookup(request):

    def request_is_valid(self):
        return 'term' in self.GET and 'app_label' in self.GET and 'model_name' in self.GET

    def get_searched_queryset(self, qs):
        model = self.mode
        term = self.GET["term"]

        try:
            term = model.autocomplete_term_adjust(term)
        except AttributeError:
            pass

        search_fields = get_autocomplete_search_fields(self.model)
        if search_fields:
            for word in term.split():
                search = [models.Q(**{smart_text(item): smart_text(word)}) for item in search_fields]
                search_qs = QuerySet(model)
                search_qs.query.select_related = qs.query.select_related
                search_qs = search_qs.filter(reduce(operator.or_, search))
                qs &= search_qs
        else:
            qs = model.objects.none()
        return qs

    def get_final_ordering(self, model, previous_lookup_parts=None):
        """
        This recursive function returns the final lookups
        for the default ordering of a model.
        Considering the models below, `get_final_ordering(Book)` will return
        `['-type__name', 'name']` instead of the simple `['-type', 'name']`
        one would get using `Book._meta.ordering`.
            class BookType(Model):
                name = CharField(max_length=50)
                class Meta:
                    ordering = ['name']
            class Book(Model):
                name = CharField(max_length=50)
                type = ForeignKey(BookType)
                class Meta:
                    ordering = ['-type', 'name']
        """
        ordering = []
        for lookup in model._meta.ordering:
            opts = model._meta
            for part in lookup.lstrip('-').split(LOOKUP_SEP):
                field = opts.get_field(part)
                if field.is_relation:
                    opts = field.rel.to._meta
            if previous_lookup_parts is not None:
                lookup = previous_lookup_parts + LOOKUP_SEP + lookup
            if field.is_relation:
                ordering.extend(self.get_final_ordering(opts.model, lookup))
            else:
                ordering.append(lookup)
        return ordering

    def get_queryset(self):
        qs = super(pacientesLookup, self).get_queryset()
        qs = self.get_filtered_queryset(qs)
        qs = self.get_searched_queryset(qs)

        if connection.vendor == 'postgresql':
            ordering = self.get_final_ordering(self.model)
            distinct_columns = [o.lstrip('-') for o in ordering]
            pk_name = self.model._meta.pk.name
            if pk_name not in distinct_columns:
                distinct_columns.append(pk_name)
            return qs.order_by(*ordering).distinct(*distinct_columns)

        return qs.distinct()

    def get_data(self):
        return [{"value": f.pk, "label": get_label(f)} for f in self.get_queryset()] //fix

    def get(self, request, *args, **kwargs):
        self.GET = self.request.GET

        if self.request_is_valid():
            self.get_model()
            data = self.get_data()
            if data:
                return JsonResponse(data)

    data = [{'id': prev[0], 'nombre': prev[1]} for prev in Paciente.op_prevision]
    return JsonResponse(data, safe=False)

#    return HttpResponse(element)
#    return render(request, '../templates/index.html')
