from django.shortcuts import render, render_to_response
from django.template import RequestContext
#from django.http import HttpResponse
from main.models import State, City
#from django.views.decorators.csrf import csrf_exempt
#from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

#forms 
from main.forms import CitySearchForm, CreateCityForm, CityEditForm

@login_required
def city_delete(request, pk):

	City.objects.get(pk=pk).delete()

	return redirect('/city_search/')

@login_required
def city_edit(request, pk):
	request_context = RequestContext(request)
	context = {}

	city = Cty.objects.get(pk=pk)

	form = CityEditForm(request.POST or None, instance=city)

	context['form'] = form 

	if form.is_valid():
		form.save()

		return redirect('/state_list/')

	return render_to_response('city_edit.html', context, context_instance=request_context)





def city_create(request):
	request_context = RequestContext(request)
	context = {}

	if request.method == 'POST':
		form = CreateCityForm(request.POST)
		context['form'] = form 

		if form.is_valid():
			form.save()


			return render_to_response('city_create.html', context, context_instance=request_context)

		else:
			context['valid'] = form.errors
			return render_to_response('city_create.html', context, context_instance=request_context)

	else:
		form = CreateCityForm()
		context['form'] = form
		return render_to_response('city_create.html', context, context_instance=request_context)


def city_search(request):
	request_context = RequestContext(request)

	context = {}

	if request.method == 'POST':
		form = CitySearchForm(request.POST)
		context['form'] = form
		if form.is_valid():
			name = '%s' % form.cleaned_data['name']
			state = form.cleaned_data['state']

			context['city_list'] = City.objects.filter(name__startswith=name, state__name__startswith=state)
			return render_to_response('city_search.html', context, context_instance=request_context)

		else:
			context['valid'] = form.errors 

	else:
		form = CitySearchForm()
		context['form'] = form

		return render_to_response('city_search.html', context, context_instance=request_context)


def state_list(request):

	context = {}
	states = State.objects.all()
	context['states'] = states 
	return render(request, 'state_list.html', context)


class StateListView(ListView):
	model = State
	template_name = 'state_list.html'
	context_objects_name = 'state'


def state_detail(request, pk):

	context = {}
	state = State.objects.get(pk=pk)
	context['state'] = state
	return render(request, 'state_detail.html', context)


class StateDetailView(DetailView):
	model = State
	template_name = 'state_detail.html'
	context_objects_name = 'state'




# def first_view(request, starts_with):
# 	states = State.objects.all()
# 	text_string = ''

# 	for state in states:
# 		cities = state.city_set.filter(name__startswith="%s" % starts_with)
# 		for city in cities:
# 			text_string += "State: %s , City: %s <br>" % (state, city.name)

# 	return HttpResponse(text_string)

# @csrf_exempt

# def get_post(request):

# 	if request.method == 'GET':
	
# 		city_state_string = """
# 			<form action="/get_post" method="POST">

# 			State:
# 			<br>
# 			<input type="text" name="state" >

# 			<br>

# 			City:
# 			<br>
# 			<input type="text" name="city" >

# 			<br>
# 			<br>
# 			<input type="submit" value="submit">

# 			</form>
# 		"""
# 		response = city_state_string
# 		return HttpResponse(response)

# 	elif request.method == 'POST':

# 		get_state = request.POST.get('state', None)
# 		get_city = request.POST.get('city', None)

# 		city_state_string = ""

# 		states = State.objects.filter(name__startswith="%s" % get_state)

# 		for state in states:
# 			cities = state.city_set.filter(name__startswith="%S" % get_city)

# 			for city in cities:
# 				city_state_string+= "<b>%S</b>" % (state, city.name)

# 		city_state_string+= """
# 				<form action="/get_post" method="POST">

# 				State:
# 				<br>
# 				<input type="text" name="state" >

# 				<br>

# 				City:
# 				<br>
# 				<input type="text" name="city" >

# 				<br>
# 				<br>
# 				<input type="submit" value="submit">

# 				</form>
# 		"""
# 		response = city_state_string
# 		return HttpResponse(response)


# def template_view(request):

# 	context = {}
# 	states = State.objects.all()
# 	context['states'] = states
# 	return render(request, 'state_list.html', context)





	