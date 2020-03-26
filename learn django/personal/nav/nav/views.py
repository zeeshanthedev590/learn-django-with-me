from django.http import HttpResponse
def ex1(request):
    sites = ['''<body bgcolor="cyan">
    <style>
    a:hover{
         color:red;
        #  box-shadow:5px 5px 5px 5px black;
    }
    </style>
    <h1>my personal navigator</H1>
    <hr>'''
 
        '''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube</a>''',
             '''<h1>For backup</h1><a href = "https://www.github.com" >github</a>''',
             '''<h1>For tuttoroals   </h1><a href = "https://www.codewithharry.com" >codewithharry</a>''',
             '''<h1>for help </h1><a href="https://w3schools.com" >w3schools</a>''',
             '''<h1>for more tuts </h1><a href="https://csdojo.io" >csdojo</a>''',
             ]
    return HttpResponse((sites))