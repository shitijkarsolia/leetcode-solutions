json_dict = {
   "qrCode":"aweqx",
   "restaurantCode":"kb_test10",
   "tableNumber":"1",
   "requestId":"e2b4e958-6833-43fa-ab1a-034c9b37d9a3",
   "currency":"USD",
   "myCurrency":[[1,2,3]],
   "calculatedTotal":2.99,
   "calculatedTotal2":{"testVal":34},
   "orderedItems":[
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
   ]
}

# Write a program that recursively converts each nested key from camelcase to snakecase

def convert_case(key):
    # helloWorld -> hello_world
    converted = ""
    for letter in key:
        if letter.islower() or letter.isdigit():
            converted = converted + letter
        else:
            converted = converted + "_" + letter.lower()
    return converted

# print(convert_case("helloWorld2"))


def convert_json(input_json):
    if type(input_json) is dict:
        output_dict ={}
        for key,val in input_json.items():
            output_dict[convert_case(key)] = convert_json(val)
        return output_dict
    elif type(input_json) is list:
        output_list =[]
        for item in input_json:
            output_list.append(convert_json(item))
        return output_list
        pass
    else:
        return input_json



print(convert_json(json_dict))
