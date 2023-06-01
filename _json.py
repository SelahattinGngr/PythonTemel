import json

person_string='{"name": "selo" , "language": ["python","css"]}'



# JSON string to Dict 
result = json.loads(person_string) # bir stirng bilgisini dictionary bilgisine dönüştürür.
result= result["language"]
#result= result["language"]
#result= result["language"][0]
print(result)
#result = json.dumps(person_string) bu abimiz de bir dictionary bilgisini string bi,lgiye dönüştürür.

