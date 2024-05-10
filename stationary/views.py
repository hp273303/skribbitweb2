
from django.shortcuts import render
from .models import TransactionItem
import requests
from django.shortcuts import redirect

# def home(request):
#     return render(request, 'index.html')

def index2(request):
    return render(request, 'index2.html')

# def wishlist(request):
#     return render(request, 'wishlist.html')


import requests
from django.shortcuts import render

def wishlist(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:8000/view_wishlist/"
    try:
        # Fetch data from the API
        response = requests.get(api_url, headers={"Authorization": "Token " + auth_token})
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            print(data)
            # Assuming you want to pass the cart data to the template
            return render(request, 'wishlist.html', {'cart_data': data,'auth_token':auth_token})
        else:
            # Handle other status codes appropriately
            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})
# def about(request):
#     api_url = "http://192.168.1.55:9000/getproductdata/view_cart/"

#     try:
        
#         response = requests.get(api_url)
        
#         if response.status_code == 200:
            
#             data = response.json()
            
#             # Filter Pens data
#             Pens_data = [item for item in data if item.get('product_name') == 'Pens']
            
#             # Categorize Pens into different categories
#             Gel_pens_data = [item for item in Pens_data if item.get('product_category') == 'Gel Pens']
#             Ball_pens_data = [item for item in Pens_data if item.get('product_category') == 'Ball Pens']
#             Roller_Ball_pens_data = [item for item in Pens_data if item.get('product_category') == 'Roller Ball Pens']
#             Premium_Gel_pens_data = [item for item in Pens_data if item.get('product_category') == 'Premium Gel Pens']
            
#             print("Gel Pens Data:", Gel_pens_data)
#             print("Ball Pens Data:", Ball_pens_data)
#             print("Roller Ball Pens Data:", Roller_Ball_pens_data)
#             print("Premium Gel Pens Data:", Premium_Gel_pens_data)
            
#             return render(request, 'about.html', {'Gel_pens_data': Gel_pens_data,
#                                                 'Ball_pens_data': Ball_pens_data,
#                                                 'Roller_Ball_pens_data': Roller_Ball_pens_data,
#                                                 'Premium_Gel_pens_data': Premium_Gel_pens_data})
#         else:
#             return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
#     except Exception as e:
#         return render(request, 'error_template.html', {'error_message': str(e)})


import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    if request.method == 'POST':
        try:
            # Get the product ID from the request
            data = json.loads(request.body)
            product_id = data.get('product_id')

            # Add logic to add the product to the cart
            # This is where you interact with your database or any other storage mechanism
            # For now, let's just print the product ID
            print("Product added to cart with ID:", product_id)

            # Return a success response
            return JsonResponse({'message': 'Product added to cart successfully'}, status=200)
        except Exception as e:
            # Return an error response if something goes wrong
            return JsonResponse({'error': str(e)}, status=500)
    else:
        # Return a method not allowed response if the request method is not POST
        return JsonResponse({'error': 'Method not allowed'}, status=405)

import requests
from django.shortcuts import render

def view_cart(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:8000/view_cart/"
    try:
        # Fetch data from the API
        response = requests.get(api_url, headers={"Authorization": "Token " + auth_token})
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            print(data)
            # Assuming you want to pass the cart data to the template
            return render(request, 'addtocart2.html', {'cart_data': data})
        else:
            # Handle other status codes appropriately
            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})



def Ball_Pens(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print (api_url)
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            pens_data = [item for item in data if item.get('product_name') == 'Pens' and item.get('product_category') == 'Ball Pens']
            print(pens_data)

            return render(request, 'Ball_Pens.html', {'data': pens_data, 'auth_token': auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def contact(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"

    try:

        response = requests.get(api_url)
        
        if response.status_code == 200:
  
            data = response.json()

            Pecil_data = [item for item in data if item.get('product_name') == 'Pencils']

            Pencil = [item for item in Pecil_data if item.get('product_category') == 'Pencil']
            Mechanical_Pencil_data = [item for item in Pecil_data if item.get('product_category') == 'Mechanical Pencil']
            Pencil_Leads_data = [item for item in Pecil_data if item.get('product_category') == 'Pencil Leads']
            Pencil_Cases_data = [item for item in Pecil_data if item.get('product_category') == 'Pencil Cases']
            
            print("Pencil:", Pencil)
            print("Mechanical_Pencil_data:", Mechanical_Pencil_data)
            print("Pencil_Leads_data:", Pencil_Leads_data)
            print("Pencil_Cases_data:", Pencil_Cases_data)
            
            return render(request, 'contact.html', {'Pencil': Pencil,
                                                'Mechanical_Pencil_data': Mechanical_Pencil_data,
                                                'Pencil_Leads_data': Pencil_Leads_data,
                                                'Pencil_Cases_data': Pencil_Cases_data,
                                                'auth_token':auth_token,
                                                })
        else:
            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})


def Erasers(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            print(data)
            
            Erasers_data = [item for item in data if item.get('product_name') == 'Erasers' and item.get('product_category') == 'Erasers']
            print(Erasers_data)

            return render(request, 'Erasers.html', {'data': Erasers_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def Folders_Fillings(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print (api_url)
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            notepads_data = [item for item in data if item.get('product_name') == 'Folders' and item.get('product_category') == 'Folders']
            print(notepads_data)

            return render(request, 'Folders_fillings.html', {'data': notepads_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})


def pen_fountain(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print(api_url)
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            
            pens_data = [item for item in data if item.get('product_name') == 'Pens' and item.get('product_category') == 'Gel Pens']
            print(pens_data)


            return render(request, 'fountain_pens.html', {'data': pens_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})


def Gel_Pens(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print (api_url)
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            pens_data = [item for item in data if item.get('product_name') == 'Pens' and item.get('product_category') == 'Gel Pens']
            print(pens_data)

            return render(request, 'Gel_Pens.html', {'data': pens_data,'auth_token': auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})


def highlighter(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print (api_url)
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            highlighters_data = [item for item in data if item.get('product_name') == 'Highlighters' and item.get('product_category') == 'Highlighters']
            print(highlighters_data)

            return render(request, 'highlighter.html', {'data': highlighters_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})
    
    
def Memo_Blocks(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            print(data)
            
            Memo_Blocks_data = [item for item in data if item.get('product_name') == 'Memo Blocks' and item.get('product_category') == 'Memo Blocks']
            print(Memo_Blocks_data)

            return render(request, 'Memo_Blocks.html', {'data': Memo_Blocks_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def notebooks(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"

    try:
        # Fetch data from the API
        response = requests.get(api_url)
        
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            
            # Filter Pens data
            notebooks_data = [item for item in data if item.get('product_name') == 'Notebooks']
            
            # Categorize Pens into different categories
            Notebooks_data = [item for item in notebooks_data if item.get('product_category') == 'Notebooks']
            Ruled_Notebooks_data = [item for item in notebooks_data if item.get('product_category') == 'Ruled Notebooks']
            Blank_Notebooks_data = [item for item in notebooks_data if item.get('product_category') == 'Blank Notebooks']

            
            print("Notebooks_data:", Notebooks_data)
            print("Ruled_Notebooks_data:", Ruled_Notebooks_data)
            print("Blank_Notebooks_data:", Blank_Notebooks_data)
            
            return render(request, 'notebooks.html', {'Notebooks_data': Notebooks_data,
                                                'Ruled_Notebooks_data': Ruled_Notebooks_data,
                                                'Blank_Notebooks_data': Blank_Notebooks_data,
                                                'auth_token':auth_token})
        else:
            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})


def notepads(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print (api_url)
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            notepads_data = [item for item in data if item.get('product_name') == 'Notepads' and item.get('product_category') == 'Notepads']
            print(notepads_data)

            return render(request, 'notepads.html', {'data': notepads_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})


def organizers(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print (api_url)
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            notepads_data = [item for item in data if item.get('product_name') == 'Desk Organizers' and item.get('product_category') == 'Desk Organizers']
            print(notepads_data)

            return render(request, 'organizers.html', {'data': notepads_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def Paperclips(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print (api_url)
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            print(data)
            pencils_data = [item for item in data if item.get('product_name') == 'Paper Clips' and item.get('product_category') == 'Paper Clips']
            print(pencils_data)

            return render(request, 'Paperclips.html', {'data': pencils_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def Premium_Gel_Pens(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            print(data)
            
            pens_data = [item for item in data if item.get('product_name') == 'Pens' and item.get('product_category') == 'Roller Ball Pens']
            print(pens_data)

            return render(request, 'Roller_Ball_Pens.html', {'data': pens_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})


def Roller_Ball_Pens(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            print(data)
            
            pens_data = [item for item in data if item.get('product_name') == 'Pens' and item.get('product_category') == 'Roller Ball Pens']
            print(pens_data)

            return render(request, 'Roller_Ball_Pens.html', {'data': pens_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})


def Shopners(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            print(data)
            
            Sharpeners_data = [item for item in data if item.get('product_name') == 'Sharpeners' and item.get('product_category') == 'Sharpeners']
            print(Sharpeners_data)

            return render(request, 'Sharpener.html', {'data': Sharpeners_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})


def Staplers(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            print(data)
            
            Sharpeners_data = [item for item in data if item.get('product_name') == 'Staplers' and item.get('product_category') == 'Staplers']
            print(Sharpeners_data)

            return render(request, 'Staplers.html', {'data': Sharpeners_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def Sticky_Notes(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            print(data)
            
            Sticky_Notes_data = [item for item in data if item.get('product_name') == 'Sticky Notes' and item.get('product_category') == 'Sticky Notes']
            print(Sticky_Notes_data)

            return render(request, 'Sticky_Notes.html', {'data': Sticky_Notes_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def todolist(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            print(data)
            
            To_Do_List_data = [item for item in data if item.get('product_name') == 'To Do List' and item.get('product_category') == 'To Do List']
            print(To_Do_List_data)

            return render(request, 'To-do_list.html', {'data': To_Do_List_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})


def aboutus(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print (api_url)
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            print(data)
            pencils_data = [item for item in data if item.get('product_name') == 'Pencils' and item.get('product_category') == 'Pencil']
            print(pencils_data)

            return render(request, 'contact.html', {'data': pencils_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})


def cancelation(request):
    return render(request, 'cancelation_policy.html')


def return_policy(request):
    return render(request, 'return_policy.html')


def refund_policy(request):
    return render(request, 'refund_policy.html')


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def terms_conditions(request):
    return render(request, 'terms_conditions.html')


def shipping_policy(request):
    return render(request, 'shipping_policy.html')


def my_account(request):
    return render(request, 'my_account.html')


def faq(request):
    return render(request, 'faq.html')


def registration(request):
    return render(request, 'registration.html')


def scissors(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print (api_url)
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            print(data)
            pencils_data = [item for item in data if item.get('product_name') == 'Scissors' and item.get('product_category') == 'Scissors']
            print(pencils_data)

            return render(request, 'scissors.html', {'data': pencils_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def calculators(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print (api_url)
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            print(data)
            pencils_data = [item for item in data if item.get('product_name') == 'Calculators' and item.get('product_category') == 'Calculators']
            print(pencils_data)

            return render(request, 'calculators.html', {'data': pencils_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def files(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print (api_url)
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            notepads_data = [item for item in data if item.get('product_name') == 'Folders' and item.get('product_category') == 'Folders']
            print(notepads_data)

            return render(request, 'Folders_fillings.html', {'data': notepads_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def pen_stands(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print (api_url)
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            print(data)
            pencils_data = [item for item in data if item.get('product_name') == 'Pen Stand' and item.get('product_category') == 'Pen Stand']
            print(pencils_data)

            return render(request, 'pen_stands.html', {'data': pencils_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def cutters(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print (api_url)
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            print(data)
            pencils_data = [item for item in data if item.get('product_name') == 'Cutters' and item.get('product_category') == 'Cutters']
            print(pencils_data)

            return render(request, 'cutters.html', {'data': pencils_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def download_app(request):
    return render(request, 'download_app.html')


def white_board_markers(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print (api_url)
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            print(data)
            pencils_data = [item for item in data if item.get('product_name') == 'White Board Markers' and item.get('product_category') == 'White Board Markers']
            print(pencils_data)

            return render(request, 'white_board_markers.html', {'data': pencils_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def punches(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print (api_url)
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            print(data)
            pencils_data = [item for item in data if item.get('product_name') == 'Punches' and item.get('product_category') == 'Punches']
            print(pencils_data)

            return render(request, 'punches.html', {'data': pencils_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def tape_dispenser(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print (api_url)
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            print(data)
            pencils_data = [item for item in data if item.get('product_name') == 'Tape Dispenser' and item.get('product_category') == 'Tape Dispenser']
            print(pencils_data)

            return render(request, 'tape_dispenser.html', {'data': pencils_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def paints(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print (api_url)
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            print(data)
            pencils_data = [item for item in data if item.get('product_name') == 'Paints' and item.get('product_category') == 'Paints']
            print(pencils_data)

            return render(request, 'paints.html', {'data': pencils_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def art_pencils(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print (api_url)
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            print(data)
            pencils_data = [item for item in data if item.get('product_name') == 'Art Pencils' and item.get('product_category') == 'Art Pencils']
            print(pencils_data)

            return render(request, 'art_pencils.html', {'data': pencils_data, 'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def art_pencils_my_view(request):
    auth_token = request.session.get('auth_token')
    return render(request, 'art_pencils.html', {'auth_token': auth_token})



def brush_pens(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print (api_url)
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            print(data)
            pencils_data = [item for item in data if item.get('product_name') == 'Brush Pens' and item.get('product_category') == 'Brush Pens']
            print(pencils_data)

            return render(request, 'brush_pens.html', {'data': pencils_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def brushes(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print (api_url)
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            print(data)
            pencils_data = [item for item in data if item.get('product_name') == 'Brushes' and item.get('product_category') == 'Brushes']
            print(pencils_data)

            return render(request, 'brushes.html', {'data': pencils_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def sketch(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    print (api_url)
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            print(data)
            pencils_data = [item for item in data if item.get('product_name') == 'Sketch' and item.get('product_category') == 'Sketch']
            print(pencils_data)

            return render(request, 'sketch.html', {'data': pencils_data,'auth_token':auth_token})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})



from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import TransactionItem

def generate_pdf(request):
    items = TransactionItem.objects.all()
    total = sum(item.total for item in items)
    
    template_path = 'bill.html'
    context = {'items': items, 'total': total}
    
    template = get_template(template_path)
    html = template.render(context)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="transaction_bill.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response

from .forms import RegistrationForm
import requests

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


# def getproduct(request):
#     api_url = "http://192.168.1.36:7000/getproductdata/"
    
#     try:
#         # Fetch data from the API
#         response = requests.get(api_url)
#         if response.status_code == 200:
#             # Convert the response to JSON
#             data = response.json()
#             # Pass the data to the template
#             return render(request, 'data_template.html', {'data': data})
#         else:
#             # If there's an error in fetching data, return an error message
#             return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
#     except Exception as e:

#         return render(request, 'error_template.html', {'error_message': str(e)})

import requests
from django.shortcuts import render
def getproduct(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    api_url = "http://192.168.1.55:9000/getproductdata/"
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            
            # Filter data for items with product name "Pens"
            pens_data = [item for item in data if item.get('product_name') == 'Pens']
        
            
            # Pass the filtered data to the template
            return render(request, 'data_template.html', {'data': pens_data})
        else:
            # If there's an error in fetching data, return an error message
            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

import requests

def getproduct(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)
    
    api_url = "http://192.168.1.55:9000/getproductdata/"
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            
            # Filter data for items with product name "Pen" and category "Ball Pen"
            pens_data = [item for item in data if item.get('product_name') == 'Pens' and item.get('product_category') == 'Ball Pen']
            # print(pens_data)

            return render(request, 'data_template.html', {'data': pens_data})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})



import requests
from django.shortcuts import render
from django.http import JsonResponse

from django.shortcuts import redirect

def register_with_api(request):
    if request.method == 'POST':
        api_url = 'http://192.168.1.55:8000/register/'

        # Validate form data
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')  # Optional field
        password = request.POST.get('password')

        if not (username and name and email and password):
            return JsonResponse({'error': 'Missing required fields'})

        # Sanitize input
        username = username.strip()
        name = name.strip()
        email = email.strip()
        phone = phone.strip()

        user_data = {
            'username': username,
            'name': name,
            'email': email,
            'phone': phone,
            'password': password,
        }

        try:
            response = requests.post(api_url, data=user_data)

            if response.status_code == 200:
                # Registration successful, redirect to the login page
                return redirect('login')  # Replace 'login' with the name of your login URL pattern
            else:
                # Registration failed, provide more details about the error
                error_message = f"Registration failed with status code {response.status_code}."
                if response.text:
                    error_message += f" Response from server: {response.text}"
                return JsonResponse({'error': error_message})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': f"Failed to connect to API server: {str(e)}"})
    else:
        return render(request, 'registration_form.html')

# import requests
# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# import json
# def login_with_api(request):
#     if request.method == 'POST':
#         api_url = 'http://192.168.1.38:8000/login/'
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         print(username)
#         print(password)

#         if not (username and password):
#             return JsonResponse({'error': 'Missing username or password'})

#         user_data = {
#             'username': username,
#             'password': password,
#         }

#         try:
#             response = requests.post(api_url, data=user_data)
#             response_content = response.content
#             response_data = json.loads(response_content)
#             status_value = response_data["status"]
#             print(status_value)

#             if status_value:
#                 # Redirect to home page on successful login
#                 return redirect('home')  # Redirect to 'home' URL
#             else:
#                 error_message = 'Invalid username or password'
#                 if response.text:
#                     error_message = response.json().get('error', error_message)
#                 return JsonResponse({'error': error_message})
#         except requests.exceptions.RequestException as e:
#             return JsonResponse({'error': f"Failed to connect to API server: {str(e)}"})
#     else:
#         return render(request, 'login_form.html')


# views.py

# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# import json
# import requests

# def login_with_api(request):
#     if request.method == 'POST':
#         api_url = 'http://192.168.1.38:8000/login/'
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         if not (username and password):
#             return JsonResponse({'error': 'Missing username or password'})

#         user_data = {
#             'username': username,
#             'password': password,
#         }

#         try:
#             response = requests.post(api_url, data=user_data)
#             response_data = response.json()
#             response_data2 = response.content
#             print(response_data2)

#             if response_data.get('status'):
#                 # Store authentication token in session
#                 request.session['auth_token'] = response_data['token']  # Use response_data here
#                 # Redirect to home page on successful login
#                 return redirect('home')
#             else:
#                 error_message = 'Invalid username or password'
#                 if response_data.get('error'):
#                     error_message = response_data['error']
#                 return JsonResponse({'error': error_message})
#         except requests.exceptions.RequestException as e:
#             return JsonResponse({'error': f"Failed to connect to API server: {str(e)}"})
#     else:
#         return render(request, 'login_form.html')





# views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests

def login_with_api(request):
    if request.method == 'POST':
        api_url = 'http://192.168.1.55:8000/login/'
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not (username and password):
            return JsonResponse({'error': 'Missing username or password'})

        user_data = {
            'username': username,
            'password': password,
        }

        try:
            response = requests.post(api_url, data=user_data)
            response_data = response.json()

            if response_data.get('status'):
                # Store authentication token in session
                request.session['auth_token'] = response_data['token']
                # Redirect to user profile page on successful login
                return redirect('user_profile2')
            else:
                error_message = 'Invalid username or password'
                if response_data.get('error'):
                    error_message = response_data['error']
                return JsonResponse({'error': error_message})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': f"Failed to connect to API server: {str(e)}"})
    else:
        return render(request, 'login_form.html')


from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests

def user_profile2(request):
    auth_token = request.session.get('auth_token')

    if auth_token:
        headers = {'Authorization': f'Token {auth_token}'}
        api_url = 'http://192.168.1.55:8000/Profile_data/'

        try:
            response = requests.get(api_url, headers=headers)
            print("Request Headers:", response.request.headers)  
            print("Response:", response.json())  

            if response.status_code == 200:
                profile_data = response.json()
                print(profile_data)
                return render(request, 'index.html' , {'profile_data': profile_data})
            else:
                return JsonResponse({'error': 'Failed to fetch user profile data'}, status=response.status_code)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': f"Failed to connect to API server: {str(e)}"})
    else:
        return redirect('login')


import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect

def user_profile(request):
    auth_token = request.session.get('auth_token')

    if request.method == 'GET':
        if auth_token:
            headers = {'Authorization': f'Token {auth_token}'}
            api_url = 'http://192.168.1.55:8000/Profile_data/'

            try:
                response = requests.get(api_url, headers=headers)
                print("Request Headers:", response.request.headers)  # Print request headers for debugging
                print("Response:", response.json())  # Print response for debugging

                if response.status_code == 200:
                    profile_data = response.json()
                    print(profile_data)
                    return render(request, 'profile.html', {'profile_data': profile_data})
                else:
                    return JsonResponse({'error': 'Failed to fetch user profile data'}, status=response.status_code)
            except requests.exceptions.RequestException as e:
                return JsonResponse({'error': f"Failed to connect to API server: {str(e)}"})
        else:
            return redirect('login')

    elif request.method == 'POST':
        if auth_token:
            headers = {'Authorization': f'Token {auth_token}'}
            api_url = 'http://192.168.1.55:8000/Profile_data/'

            try:
                # Assuming you have the updated profile data in request.POST or request.data
                # Assuming profile photo is updated via file upload
                data = {
                    'name': request.POST.get('name'),
                    'email': request.POST.get('email'),
                    'mobile': request.POST.get('mobile'),
                    'username': request.POST.get('username'),
                }

                files = {}
                if request.FILES.get('image'):
                    files = {'image': request.FILES['image']}

                response = requests.put(api_url, headers=headers, data=data, files=files)

                print("Request Headers:", response.request.headers)  # Print request headers for debugging
                print("Response:", response.json())  # Print response for debugging

                if response.status_code == 200:
                    return JsonResponse({'success': 'User profile updated successfully'})
                else:
                    return JsonResponse({'error': 'Failed to update user profile'}, status=response.status_code)
            except requests.exceptions.RequestException as e:
                return JsonResponse({'error': f"Failed to connect to API server: {str(e)}"})
        else:
            return redirect('login')

from django.shortcuts import render

def about(request):
    auth_token = request.session.get('auth_token')
    print(auth_token)

    api_url = "http://192.168.1.55:9000/getproductdata/"

    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Filter Pens data
            Pens_data = [item for item in data if item.get('product_name') == 'Pens']
            
            # Categorize Pens into different categories
            Gel_pens_data = [item for item in Pens_data if item.get('product_category') == 'Gel Pens']
            Ball_pens_data = [item for item in Pens_data if item.get('product_category') == 'Ball Pens']
            Roller_Ball_pens_data = [item for item in Pens_data if item.get('product_category') == 'Roller Ball Pens']
            Premium_Gel_pens_data = [item for item in Pens_data if item.get('product_category') == 'Premium Gel Pens']
            
            print("Gel Pens Data:", Gel_pens_data)
            print("Ball Pens Data:", Ball_pens_data)
            print("Roller Ball Pens Data:", Roller_Ball_pens_data)
            print("Premium Gel Pens Data:", Premium_Gel_pens_data)
            
            return render(request, 'about.html', {'Gel_pens_data': Gel_pens_data,
                                                   'Ball_pens_data': Ball_pens_data,
                                                   'Roller_Ball_pens_data': Roller_Ball_pens_data,
                                                   'Premium_Gel_pens_data': Premium_Gel_pens_data,
                                                   'auth_token': auth_token})  # Pass auth_token to the template
        else:
            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})
    

def my_view(request):
    auth_token = request.session.get('auth_token')
    return render(request, 'about.html', {'auth_token': auth_token})

