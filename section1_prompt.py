
from langchain import PromptTemplate, FewShotPromptTemplate


#First, create the list of few shot examples.(which gpt will use to understand)
### few short learning examples for gpt
example_1 = [
{
"query":
        """
        Dear GPT,
        I need your help in rewriting an application for a new applicant. Please follow the exact structure and style of the template application below
        kindly please do not generate anything else only the application. Your are restricted to generate line numbering exactly as in the template application. which are 1.1.1 to 1.1.4.
        template Application:
        1.1.1. Contour Town Planning has been tasked with preparing a planning statement on behalf of Philip John Myerscough for an application to the City of Edinburgh Council. The purpose of this application is to obtain a Certificate of Lawfulness of Existing Use or Development for the property located at Flat 2F1, 57 Merchiston Crescent, Edinburgh EH10 5AH.
        1.1.2. The property has been used as a short-term let since January 2019, with a temporary cessation from September 2019 to June 2020, and resumed in Autumn 2020. This application aims to demonstrate that the use of the property as a short-term let does not constitute a material change of use under Section 150 (2) of the Town and Country Planning (Scotland) Act 1997.
        1.1.3. The property has three bedrooms, but only two are used for short-term letting, accommodating a maximum of four people. The remaining bedroom and a storage cupboard are retained for the owner's personal use.
        1.1.4. The applicant purchased the property in 2009 and extensively renovated it to create a modern and comfortable family home. The property is located in a sought-after part of Edinburgh, offering views of the stone-built villas opposite and convenient access to public transport.
        The information for the new applicant is as follows:
        The information for the new applicant is as follows:
        'Time': Timestamp('2023-07-18 11:03:31.623000'),'Contract_Number#': 'ST1012', 'Full_Name': 'Julie Yvonne Hebdon', 'Email_Address': 'juleshebdon65@gmail.com', 'Unique_Features': ' Main door accessible flat directly onto Melbourne Road', 'Property_Location': '17 Melbourne Road, North Berwick EH39 4JX. Part of a residential stone,  built approx 1900,  block of flats. We are ground floor main door access, directly opposite Milsey Beach in North Berwick. There are no properties overlooking the flat. The surrounding properties are a mix of residential & holiday let’s. The flat is within walking distance to beach less than  50m  & shops/restaurants less than 500m from the property.', 'Proximity_to_POI': 'Coastal Communities Museum 100m. Scottish Seabird Centre 100m.', 'Surroundings_Appeal': 'The property is directly opposite Milsey Beach. This appeals to guests & its proximity to shops/restaurants of North Berwick. Easy access to train station/bus links makes travel available to all that visit. Free on street parking outside the flat also.', 'Occupancy_Rules': 'Maximum occupancy 4. No hen or stag parties permitted. Free on street parking directly outside the flat & in neighbouring streets but also within close proximity to car parks that are within walking distance. No guests have ever complained of lack of parking. Period of use varies with individual bookings, from long weekends to fortnight bookings. Out of season minimum night stay is usually 3 nights whilst in high season this will be 7 nights. We accommodate predominantly families or couples & also allow 2 small dogs. We have never had any issues of disturbance/noise with any of the guests that have stayed or from residents neighbouring our property. Our management company Coast Properties would be able to verify that no complaints have been received regarding the issues stated above.', 'Minimum_Stay': '3 nights in low season. 7 nights in high season. Coast Properties, the management company for Breakwater have provided 10 year continuous holiday let information together with bookings for the last financial year to support this application. We purchased the property in August 2020. At this time this property formally called Aviemore was marketed by Coast Properties & had been so for the previous 10 years. We have maintained this relationship, keeping the marketing of Breakwater (formally Aviemore) from purchase to date.', 'Guest_Screening': 'No hen or stag parties permitted with a max of 2 dogs allowed. Guest screening/vetting is completed by our management company Coast Properties. Predominantly our bookings are repeat business from guests from one year to the next. We have never experienced any guest being declined a booking or future booking but this is covered within T&Cs of booking with Coast Properties.', 'House_Rules': 'There is a guest “Breakwater Handbook” communicating all info regarding their booking. All that the guest may require from contact info for Coast Properties, the cleaning team CleanTec, contact information for emergencies be that police/fire or hospital details. An insight into the local area & what they can expect from their visit re attractions/sights of interest. There is also in situ a “Breakwater Appliance Guide” detailing all they need to know & how the heating/water works etc. Also in situ is a  “Breakwater Important Info” this includes EPC, Legionella Certificate of Compliance, PAT Report/Certificate, EICR, Fire Risk Assessment Report. All these are up to date & there are procedures in place to ensure that they remain so. Guests have peace of mind that their safety during their stay is considered with regular maintenance of both smoke detectors, fire extinguisher & first aid kit regularly carried out. This can also be evidenced.', 'Guest_Documentation': 'In situ “Breakwater Handbook” gives guests details on who to contact should they have any concerns during their stay. We have had no instances of noise/bad behaviour since owning the property ', 'Guest_Access': 'There is a key safe beside the main door access to the flat that opens directly on to the street, Melbourne Road. Spare set keys are provided once inside the property. Should guests lose keys then another set is kept in North Berwick by Coast Properties', 'Access_Route': 'No properties overlook the flat. We are ground floor,  main door access, directly opposite Milsey Beach. We do have neighbouring flats either side of us & directly above. We are the only main door access property, to our knowledge, within the block of flats.\n', 'Parking_Facilities': 'Free on street parking directly outside flat & In neighbouring streets. Also within walking distance from car parks situated in North Berwick. The closest would be within 100m. This info is provided on the website Coast Properties & on booking ', 'Outdoor_Spaces': 'No outdoor space or storage facilities outwith the flat itself', 'Cleaning_Procedures': 'Guests are aware that the cleaning is maintained by CleanTec. Their contact details are provided within the “Breakwater Handbook” which is in the flat & easily accessible to read. Again these details are passed over on booking. When a booking is made the management company Coast Properties then pass details of length of booking directly to the cleaning team, CleanTec. These are then added to their own internal booking system to ensure smooth changeovers. Guests are asked to strip beds etc on leaving & to advise cleaning team if anything does not meet their standards on arrival. The cleaning team would then attend immediately to rectify should this be the case.', 'Complaints_Details': 'Any complaints would go, on first contact, to management company Coast Properties or CleanTec. Should the management company then require the owners to respond directly to the guests then we would be informed & would do so immediately.  Minor niggles, as with any holiday let, have been dealt with swiftly to guests satisfaction. Most recent issues  I can recall would be the key safe sticking when trying to access. This was rectified the same day by a maintenance team being on hand in North Berwick who supplied & installed a new key safe.'
        """
        ,
"answer":
        """
        1.1.1. Julie Yvonne Hebdon has assigned the responsibility of drafting a planning statement to Contour Town Planning. This application is intended to procure a Certificate of Lawfulness of Existing Use or Development from the City of Edinburgh Council, for the property at 17 Melbourne Road, North Berwick EH39 4JX.
        1.1.2. Since August 2020, the property has been utilised as a short-term let. This application seeks to validate that the property's usage as a short-term let does not signify a material change of use according to Section 150 (2) of the Town and Country Planning (Scotland) Act 1997.
        1.1.3. The flat can accommodate a maximum of four people as a short-term let, but it does not offer any external space or storage facilities outside of the property itself.
        1.1.4. The applicant bought the property in 2020 and retained the marketing of Breakwater (formerly known as Aviemore) as it was before the purchase. Situated directly opposite Milsey Beach in North Berwick, the property is part of a residential stone-built block of flats constructed around 1900. It's a ground-floor main-door accessible flat, offering direct access onto Melbourne Road. There are no properties overlooking the flat, with surrounding properties comprising a mix of residential and holiday let's. Its appeal to guests includes its proximity to shops, restaurants, and points of interest like Coastal Communities Museum and the Scottish Seabird Centre, all within walking distance.
        """
},
{
"query":
        """
        excellent work.
        great work now i will give you another input to check if you are generating okay with new information
        'Time': Timestamp('2023-07-18 11:03:31.623000'), 'Contract_Number': 'ST1015', 'Full_Name': 'ruggero baietta', 'Email_Address': 'ruggerobaietta@gmail.com', 'Unique_Features': 'Our property is ground floor and opposite Medawbank shopping centre.', 'Property_Location': 'Ground floor, residential area but very close to a commercial one. Close to buses and a busy road, but extremely quiet and private at the same time. ', 'Proximity_to_POI': 'Holyrood Palace is less than 1 km away. ', 'Surroundings_Appeal': 'The property is very close to shops and restaurants, but at the same time it is nearby Holyrood Park and the pick of Arthur Seat. ', 'Occupancy_Rules': 'The property has got a dedicated parking spot. It is part of a building so we want to limit the maximum number of occupants to 4, having a double bedroom and a twin one. The large living room with a big sofa could easily accomodate more people, but to avoid parties and other noisy activities we do not allow more people to stay at the property. \nIt is a ground floor and there is only another flat at the same floor. The property is available all through the year and so far we did not have any complain from neighbours.', 'Minimum_Stay': '2 nights is the minimum stay and the average rental is probably 5 days but I need to investigate on this. I can easily send over the Airbnb bookings.', 'Guest_Screening': 'We take bookings from Airbnb mainly and we look at reviews of the guests.', 'House_Rules': 'No parties, no smoking and no noise that might disturb the neighbours.', 'Guest_Documentation': nan, 'Guest_Access': 'Main door of the building with keys, main door of the property again with keys. There is a self check-in with a lockbox located outside the property.', 'Access_Route': nan, 'Parking_Facilities': 'There is a dedicated parking spot and a p[hoto showing it to the guest', 'Outdoor_Spaces': 'There is a common garden in front of the property and a common area for rubbish bins.', 'Cleaning_Procedures': 'We have a cleaner going in after every guest. change of bed linens and towels and deep cleaning of all the property. For guests staying over a week we can provide extra cleaning/ changing of bed linen, towels. ', 'Complaints_Details': 'No complains so far'
        """
        ,
"answer":
        """
        1.1.1. Contour Town Planning has been appointed to prepare a planning statement on behalf of Ruggero Baietta for submission to the City of Edinburgh Council. This application's aim is to secure a Certificate of Lawfulness of Existing Use or Development for the property located at the ground floor, in a residential area close to a commercial zone.
        1.1.2. The property has been serving as a short-term let since its purchase. The purpose of this application is to establish that the use of the property as a short-term let does not represent a material change of use under Section 150 (2) of the Town and Country Planning (Scotland) Act 1997.
        1.1.3. The property comprises a double bedroom and a twin bedroom, accommodating a maximum of four people to prevent parties and other noisy activities. It also features a large living room with a big sofa. There are common garden areas in front of the property and a dedicated spot for parking.
        1.1.4. The applicant acquired the property and has since made it available for short-term letting all year round, primarily through Airbnb. The property is ground floor, opposite Medawbank shopping centre, with proximity to shops, restaurants, Holyrood Park, and Arthur Seat peak."""
},
{
"query":
        """
         Excellent
         here is the new information:
        'Name': 'Philip John Myerscough', 'Full property address': 'Flat 2F1, 57 Merchiston Crescent, Edinburgh EH10 5AH', 'When did you commence trading as a short term let (approximately)': '01/2019. Ceased 09/2019. Long term let 09/2019 to 06/2020. Recommenced Autumn 2020', 'Number of bedrooms': 'The flat has 3 but we retain 1 and a store cupboard for our own use. So the flat is jet as 2 bedroom; max 4 people', 'Approximate size (sqm)': 'Total approx 135sqm Area let to tenants approx 120sqm', 'Property type (if flat describe floor, shared access, private entrance, etc)': "The flat is on the second floor. The stair serves 6 flats in total. 2 on first floor, 2 on second, 2 on third. The flat is the first on the second floor. The 2 ground floor flats in the building have their own front doors opening to the street. They each have an area of garden sheltering them from the street and the upper flats' entrance.", 'Can you provide a brief history of your ownership of property and description of the property and the area it is located in?': 'The property is a substantial 3 bedroom tenement flat constructed in 1890s in a sought after part of Edinburgh. It has views out over Edinburgh over the stone built villas opposite. Good public transport links. I bought the property in 2009 and substantially reformed it to create a modern, comfortable home for my family. I and my 2/3 children lived exclusively at the property until I retired. In mid 2018 we bought a house in Spain where we now live for most of the year.'
        """
        ,
"answer":
        """
        1.1.1. Contour Town Planning has been commissioned to prepare a planning statement for Philip John Myerscough to submit an application to the City of Edinburgh Council. The aim of this application is to obtain a Certificate of Lawfulness of Existing Use or Development for the property located at Flat 2F1, 57 Merchiston Crescent, Edinburgh EH10 5AH.
        1.1.2. The property has functioned as a short-term let since January 2019, with a temporary halt from September 2019 to June 2020, resuming operations in Autumn 2020. This application seeks to affirm that the use of the property as a short-term let does not constitute a material change of use under Section 150 (2) of the Town and Country Planning (Scotland) Act 1997.
        1.1.3. The property features three bedrooms, but only two are utilised for short-term letting, accommodating a maximum of four individuals. The remaining bedroom and a storage cupboard are reserved for the owner's personal use, making the total area let to tenants approximately 120sqm out of the total 135sqm.
        1.1.4. The applicant acquired the property in 2009 and significantly refurbished it to create a modern, comfortable home for his family. The property, constructed in the 1890s, is a substantial three-bedroom tenement flat situated in a sought-after part of Edinburgh, offering views of the stone-built villas opposite and convenient access to public transport
        """
}
]



# Next, we specify the template to format the examples we have provided.
# We use the `PromptTemplate` class for this.
example_template = """
User: {query}
AI: {answer}
"""
example_prompt = PromptTemplate(
    input_variables=["query", "answer"],
    template=example_template,
)




# Finally, we create the `FewShotPromptTemplate` object.
few_shot_prompt_1 = FewShotPromptTemplate(
    # These are the examples we want to insert into the prompt.
    examples=example_1,
    # This is how we want to format the examples when we insert them into the prompt.
    example_prompt=example_prompt,
    # The prefix is some text that goes before the examples in the prompt.
    # Usually, this consists of intructions.
    prefix = """
        ChatGPT, you are an application rewriter. Using the new applicant's details and following the structure and style of the original application, I need you to rewrite this application.
        You are an data entry and application writer for the Certificate of Lawful Use for Short-term Let Accommodation: Planning Statement.
        You will be given all the necessary information about the applicant in the input and your task is to follow a application format that will be provided and update that application text with the new information given to you as a text.
        Original Application:
        1.1.1. Contour Town Planning has been tasked with preparing a planning statement on behalf of Philip John Myerscough for an application to the City of Edinburgh Council. The purpose of this application is to obtain a Certificate of Lawfulness of Existing Use or Development for the property located at Flat 2F1, 57 Merchiston Crescent, Edinburgh EH10 5AH.
        1.1.2. The property has been used as a short-term let since January 2019, with a temporary cessation from September 2019 to June 2020, and resumed in Autumn 2020. This application aims to demonstrate that the use of the property as a short-term let does not constitute a material change of use under Section 150 (2) of the Town and Country Planning (Scotland) Act 1997.
        1.1.3. The property has three bedrooms, but only two are used for short-term letting, accommodating a maximum of four people. The remaining bedroom and a storage cupboard are retained for the owner's personal use.
        1.1.4. The applicant purchased the property in 2009 and extensively renovated it to create a modern and comfortable family home. The property is located in a sought-after part of Edinburgh, offering views of the stone-built villas opposite and convenient access to public transport.
            """,
    # The suffix is some text that goes after the examples in the prompt.
    # Usually, this is where the user input will go
    suffix = """
            User: {query}
            AI: """,
    # The input variables are the variables that the overall prompt expects.
    input_variables=["query"],
    # The example_separator is the string we will use to join the prefix, examples, and suffix together with.
    example_separator="\n\n",
)