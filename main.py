from flask import Flask, request, render_template
from gpt_config import chain1
from gpt_config import chain2
from gpt_config import chain3
from output_transform import transform
from output_transform import edit_doc
from docx import Document

app = Flask(__name__)


def automate(query, word_file_path, save_path):
    section1 = chain1.run(query=query)
    section2 = chain2.run(query=query)
    section5 = chain3.run(query=query)
    cl_s1, cl_s2, cl_s5 = transform(section1=section1, section2=section2, section5=section5)
    if len(cl_s1)==4 and len(cl_s2)==4 and len(cl_s5)==16:
        edit_doc(word_file_path, save_path, line_1=cl_s1, line_2=cl_s2, line_3=cl_s5)
        return "done"
    else:
        return"please try again"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['query']
        print(query)
        word_file_path = "word.docx"
        save_path = "output.docx"
        result = automate(query=query, word_file_path=word_file_path, save_path=save_path)
        return result
    return render_template('home.html')


if __name__ == '__main__':
    app.run(port=5003, debug=True)

# from gpt_config import chain1
# from gpt_config import chain2
# from gpt_config import chain3
# from output_transform import transform
# from output_transform import edit_doc
# from docx import Document

# def automate(query,word_file_path,save_path):
#     section1=chain1.run(query=query)
#     section2=chain2.run(query=query)
#     section5=chain3.run(query=query)
#     cl_s1,cl_s2,cl_s5 = transform(section1=section1,section2=section2,section5=section5)
#     edit_doc(word_file_path,save_path,line_1=cl_s1,line_2=cl_s2,line_3=cl_s5)
#     print("done")


# query = """
# {
# "Name": "Philip John Myerscough",
# "Full property address": "Flat 2F1, 57 Merchiston Crescent, Edinburgh EH10 5AH",
# "When did you commence trading as a short term let (approximately)":           "01/2019. Ceased 09/2019. Long term let 09/2019 to 06/2020. Recommenced Autumn 2020",
# "Number of bedrooms":                                                          "The flat has 3 but we retain 1 and a store cupboard for our own use. So the flat is jet as 2 bedroom; max 4 people",
# "Approximate size (sqm)":                                                      "Total approx 135sqm Area let to tenants approx 120sqm",
# "Property type (if flat describe floor, shared access, private entrance, etc)":"The flat is on the second floor. The stair serves 6 flats in total. 2 on first floor, 2 on second, 2 on third. The flat is the first on the second floor. The 2 ground floor flats in the building have their own front doors opening to the street. They each have an area of garden sheltering them from the street and the upper flats' entrance.",
# "Can you provide a brief history of your ownership of property and description of the property and the area it is located in?":"The property is a substantial 3 bedroom tenement flat constructed in 1890s in a sought after part of Edinburgh. It has views out over Edinburgh over the stone built villas opposite. Good public transport links. I bought the property in 2009 and substantially reformed it to create a modern, comfortable home for my family. I and my 2/3 children lived exclusively at the property until I retired. In mid 2018 we bought a house in Spain where we now live for most of the year.",
# "Are there any notable commercial establishments or public facilities that are located near the property?": "The property is 5 mins walk from Bruntsfield with its shops supermarkets, bars and restaurants. It is 3 minutes walk from Napier University",
# "Can you describe the nature of immediate surrounding area of the property (e.g residential / commercial)":"The merchiston area is residential with a mixture of tenement flats and villas. It lies close to the retail/leisure facilities available in Bruntsfield and Mmorningside",
# "Does the property have any special access (e.g. lift, concierge, accessible, etc)No":"",
# "How would you describe occupancy levels and use of the property? Do you also use for personal purposes?":"The property is popular. It is priced at the top end of the market to discourage inappropriate tenants. We have a 4.9 out of 5 rating on airbnb. Tenants are respectful and well behaved. We occasionally use the property when we visit Edinburgh. We still consider it our home in the UK. We retain all our possessions there. Our art is on the walls. It looks and feels exactly as it did when we lived there full time.",
# "How does the property and its use integrate with the character and activities of the wider area?":"The property is indistinguishable from any other in the area. I would be very surprised if anyone other than our immediate neighbours in the building were aware of the short term tenants. I am not aware of any other short term let's in the area but there are a lot of student flats which can be, and are, disruptive at night.",
# "Can you describe in detail how the property is accessed (e.g. private door, shared entrance) and how any nuisance to neighbours is minimised.":"Every tenant is met at the door to the building and escorted to the flat. To reach the flat they pass the 2 flats on the first floor. The tenants are reminded of the rules regarding noise and nuisance. The flat is fitted with a noise monitor which sends notifications of loud noise.",
# "How many bedrooms are used for the purposes of short term letting?":"2 out of 3",
# "How many guests can the property comfortably accommodate and is this consistent with a residential property in the area?":"We set a maximum of 4. Nearly all the flats in the area have 3 double bedrooms and can easily accommodate 6. The villas are much larger.",
# "How has the size of the property influenced any decisions regarding its use or layout (for instance, not installing a sofa bed to limit occupants)?":"The property could easily accommodate 6 people. There is a large lounge but no sofa beds. We limit the number of tenants to 4 to control the profile of visitors to protect the fabric of our home and possessions",
# "What is the minimum and maximum duration guests can book the property?":"Minimum 2 nights. There is no maximum.",
# "What is the typical duration of stay for guests?":"Typically 3 or 4 nights out of season, 5 to 7 in season. In July and August 2 or 3 weeks is not uncommon.",
# "How are potential guests screened or vetted before booking?":"They must have proven ID. Our agent vets and approves every request to book. We reject groups of single young people",
# "What are the property's house rules, and how are they enforced to manage guest behaviour?":"No noise, silence after 11pm, no dogs, no parties, nobody to be invited to the property. Tenants are told noise is monitored and the agent lives 10 minutes walk round the corner. They are told they will be ejected for breach in accordance with airbnb policy.",
# "Do you use any devices to monitor use (for example, noise monitoring, video doorbells, electronic locks)":"Internet enabled app based, noise monitoring",
# "What type of visitors does your property normally attract (e.g. families, corporate workers, etc)":"Families from abroad particularly China.",
# "Is there any access provided to shared spaces or is this restricted to respect neighbours?":"Access to shared back green is forbidden. It is locked and only available to neighbours.",
# "What arrangements are made for parking, bag storage, or other guest needs?":"Parking is controlled by the Council. Rules and costs are explained in our airbnb entry. Our guests typically arrive by air or train. There is lots of room in the property to store bags.",
# "How are cleaning and maintenance of the property scheduled and performed?":"Cleaning is carried out after every guest leaves under supervision by the agent. Maintenance is organised by the agent in conjuction with ourselves.",
# "How do you ensure minimal disruption to guests and neighbours during cleaning and maintenance activities?":"Cleaning and maintenance are carried out by professionals during normal business ours. There is no disruption."


# }"""


# word_file_path = "word.docx"
# save_path = "output.docx"
# automate(query=query,word_file_path=word_file_path,save_path=save_path)
