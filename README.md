# dokkanz

First I would like to thanks to give the opportunity to apply for this job .

How to build a good API ?
As API is the most important concept to release a project can be accessed from (web , mobile ,….etc)
so first should take care of some important points :
1- good understanding for the project requirements for all platform will calling your API`s endpoints.
2-set a clear scenarios for consuming this end point response dose it easy for fronted developer to use ? Dose it satisfy the need ?.
3- walleyes be carefully to return specified response or message to clearly show the data ,errors, response type .
4-be sure your authentication method tokens are protected (try to use official 3 rd party libraries ) not to handle it your self except need more configurations.
5-if your end point will only consumed with your single page application hocked in landing template ? Be sure to close all whitelist and cors headers origins for you app only.
6-always make a good docs for every function , end-point and class you create.
7-test your app with different ways (postman,django-restframework interface, js SPA fired in other localhost ip,….)
8-for the authorizations django DRF has a great remissions classes tool would help the developer to customize your authorizations and permissions   .




the task documentation: 

 the task  have the following behaviour :

1-creating model for category.
2-to make it dynamic adding ,delleting ,..i used modelViewSet will handel all this point N.B :it made without premission class this means any user or anyounmes request can mobultae it.
Category endpoint:
http://127.0.0.1:8000/categories/   with GET return a list of  catagoires as [
    {
        "id": 1,
        "name": "Iphone"
    }
]

http://127.0.0.1:8000/categories/   with Post  data must include object{‘name’:’catagory name’}
response :
{
    "id": 2,
    "name": "test5"
}
http://127.0.0.1:8000/categories/ {id}/ with get for retrive 
reposne for http://127.0.0.1:8000/categories/ 1/ 
{
    "id": 1,
    "name": "Iphone"
}
 same for put patch for updates
for delete respnse 200 ok


product End point


http://127.0.0.1:8000/product/

the response will be with list of product have nasted category details and paginated with max  5 products every page :

"count": 47,
    "next": "http://127.0.0.1:8000/product/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "test1",
            "Product_code": "A3s17",
            "price": "13.55",
            "quantity": 155,
            "categories": [
                {
                    "id": 1,
                    "name": "Iphone"
                }
            ]
        },
        {
            "id": 2,
            "name": "tes 2",
            "Product_code": "As255",
            "price": "12.55",
            "quantity": 20,
            "categories": [
                {
                    "id": 1,
                    "name": "Iphone"
                }
            ]
        },



 
http://127.0.0.1:8000/product/{1}/

retrive product details 
{
    "id": 1,
    "name": "test1",
    "Product_code": "A3s17",
    "price": "13.55",
    "quantity": 155,
    "categories": [
        {
            "id": 1,
            "name": "Iphone"
        }
    ]
}
for delete update and patch should pass the category ID only 

example for http://127.0.0.1:8000/product/{1}/
{
    
    "name": "test1",
    "Product_code": "A3s17",
    "price": "13.55",
    "quantity": 155,
    "categories": [
        1
    ]
}



 all requirements will be found in requirement.txt inside the app folder
cors headers is activated for accepting any requests


githublink:





thanks for the great time I spent to this task 
