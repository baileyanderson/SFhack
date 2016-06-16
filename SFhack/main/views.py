from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from main.models import FAQ
from operator import itemgetter

def index(request):
	#listIn2 = FAQ.objects.order_by('id')[:5]
	#keywordsInQuestion = ['claim', 'status', 'pizza', 'cat']
	f = open("C:/Users/BAILEY/Programming/hackathon/stateFarm/pipe.txt", "r")
	allKeys = f.read()

	keywordsInQuestion = allKeys.split(",")

	print(keywordsInQuestion)
	FAQall = []
	dicta = {}
	dicta2 = []

	for i in range (0, len(keywordsInQuestion)):
		FAQall.append(FAQ.objects.filter(keywords__contains=keywordsInQuestion[i]))

	for faq in range (0, len(FAQall[0])):
		dicta[FAQall[0][faq]] = 1

	for qSet in range (1, len(FAQall)):	
		for faq in range (0, len(FAQall[qSet])):
			if FAQall[qSet][faq] in dicta: #already in dict
				dicta[FAQall[qSet][faq]] = dicta[FAQall[qSet][faq]] + 1
			else:
				dicta[FAQall[qSet][faq]] = 1

	#dicta = sorted(dicta.items(), key=itemgetter(2))
	dicta = sorted(dicta.items(), key=itemgetter(1), reverse = True)
	for i in range(0, len(dicta)):
		dicta2.append(dicta[i][0])
		#print(thing[1])
		#print(thing[0])

	context = {
		'dicta' : dicta2,
		#'dicta2' : dicta[0],
	}
	#return HttpResponse(template.render(context, request))
	return render(request, 'main/index.html', context)