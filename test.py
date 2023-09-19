def camel_to_snake_case(name):
    result = []
    for char in name:
        if char.isupper():
            result.append('_' + char.lower())
        else:
            result.append(char)
    return ''.join(result)

def convert_keys_to_snake_case(data):
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            new_key = camel_to_snake_case(key)
            new_value = convert_keys_to_snake_case(value)
            new_dict[new_key] = new_value
        return new_dict
    elif isinstance(data, list):
        new_list = []
        for item in data:
            new_list.append(convert_keys_to_snake_case(item))
        return new_list
    else:
        return data

json_dict = {
   "qrCode":"aweqx",
   "restaurantCode":"kb_test10",
   "tableNumber":"1",
   "requestId":"e2b4e958-6833-43fa-ab1a-034c9b37d9a3",
   "currency":"USD",
   "myCurrency":[[1,2,3]],
   "calculatedTotal":2.99,
   "calculatedTotal2":{"testVal":34},
   "orderedItems":[[
      {
         "myId":999966,
         "displayPrice":"0",
         "timestamp":"",
         "tax":"0",
         "taxList":[
            {
               "amountName":"0",
               "label":"tax",
               "timestampToday":"dfdf"
            },
            {
               "personalNo":"0",
               "myTax":"ta3x",
               "timestampTomorrow":"wed"
            }
         ]
      }
   ]]
}


converted_json = convert_keys_to_snake_case(json_dict)
print(converted_json)