
from langchain import PromptTemplate, FewShotPromptTemplate


### few short learning examples for gpt

example_2 =[

{
"query":
        """
        Dear GPT,
        I need your help in rewriting an application for a new applicant. Please follow the exact structure and style of the template application below
        kindly please do not generate anything else only the application. Your are restricted to generate line numbering exactly as in the template application. which are 2.1.1 to 2.1.4.
        template Application:
        Property Description and Surroundings
        2.1.1. The property in question is a historically significant flat situated at Breakwater, 17 Melbourne Road, North Berwick EH39 4JX. These flat houses carry cultural significance and are well-regarded within the city. The current owner of the property acquired it in September 2020.
        2.1.2. Inside the property, there is one double bedroom and one twin bedroom, allowing accommodation for up to four guests. The property owner has made a conscious decision not to include a sofa bed in the living room to maintain a peaceful environment and prioritize the comfort of both guests and neighbors. By limiting the number of occupants and avoiding potential noise disturbances, the residential character of the property is preserved. Additionally, this decision aligns with the property's intended use for short-term guest accommodation, rather than long-term residency, which helps avoid any changes that could affect its permitted use.
        2.1.3. The property can be accessed through the front door, which directly faces Melbourne Road. To secure the property, a key box has been installed at the front door. Inside the flat, there is a key safe beside the main door access, also facing Melbourne Road. Spare set keys are provided within the property. In case guests lose their keys, another set is kept in North Berwick by Coast Properties.
        2.1.4. There is free on-street parking available right outside the flat and in nearby streets. Furthermore, the property is conveniently located within walking distance from car parks situated in North Berwick. This preference further supports the argument that the property's use for short-term guest accommodation has a minimal impact on parking demand compared to the requirements of long-term residents.
        
        The information for the new applicant is as follows:
        'Time': Timestamp('2023-07-18 11:03:31.623000'),'Contract_Number#': 'ST1012', 'Full_Name': 'Julie Yvonne Hebdon', 'Email_Address': 'juleshebdon65@gmail.com', 'Unique_Features': ' Main door accessible flat directly onto Melbourne Road', 'Property_Location': '17 Melbourne Road, North Berwick EH39 4JX. Part of a residential stone,  built approx 1900,  block of flats. We are ground floor main door access, directly opposite Milsey Beach in North Berwick. There are no properties overlooking the flat. The surrounding properties are a mix of residential & holiday let’s. The flat is within walking distance to beach less than  50m  & shops/restaurants less than 500m from the property.', 'Proximity_to_POI': 'Coastal Communities Museum 100m. Scottish Seabird Centre 100m.', 'Surroundings_Appeal': 'The property is directly opposite Milsey Beach. This appeals to guests & its proximity to shops/restaurants of North Berwick. Easy access to train station/bus links makes travel available to all that visit. Free on street parking outside the flat also.', 'Occupancy_Rules': 'Maximum occupancy 4. No hen or stag parties permitted. Free on street parking directly outside the flat & in neighbouring streets but also within close proximity to car parks that are within walking distance. No guests have ever complained of lack of parking. Period of use varies with individual bookings, from long weekends to fortnight bookings. Out of season minimum night stay is usually 3 nights whilst in high season this will be 7 nights. We accommodate predominantly families or couples & also allow 2 small dogs. We have never had any issues of disturbance/noise with any of the guests that have stayed or from residents neighbouring our property. Our management company Coast Properties would be able to verify that no complaints have been received regarding the issues stated above.', 'Minimum_Stay': '3 nights in low season. 7 nights in high season. Coast Properties, the management company for Breakwater have provided 10 year continuous holiday let information together with bookings for the last financial year to support this application. We purchased the property in August 2020. At this time this property formally called Aviemore was marketed by Coast Properties & had been so for the previous 10 years. We have maintained this relationship, keeping the marketing of Breakwater (formally Aviemore) from purchase to date.', 'Guest_Screening': 'No hen or stag parties permitted with a max of 2 dogs allowed. Guest screening/vetting is completed by our management company Coast Properties. Predominantly our bookings are repeat business from guests from one year to the next. We have never experienced any guest being declined a booking or future booking but this is covered within T&Cs of booking with Coast Properties.', 'House_Rules': 'There is a guest “Breakwater Handbook” communicating all info regarding their booking. All that the guest may require from contact info for Coast Properties, the cleaning team CleanTec, contact information for emergencies be that police/fire or hospital details. An insight into the local area & what they can expect from their visit re attractions/sights of interest. There is also in situ a “Breakwater Appliance Guide” detailing all they need to know & how the heating/water works etc. Also in situ is a  “Breakwater Important Info” this includes EPC, Legionella Certificate of Compliance, PAT Report/Certificate, EICR, Fire Risk Assessment Report. All these are up to date & there are procedures in place to ensure that they remain so. Guests have peace of mind that their safety during their stay is considered with regular maintenance of both smoke detectors, fire extinguisher & first aid kit regularly carried out. This can also be evidenced.', 'Guest_Documentation': 'In situ “Breakwater Handbook” gives guests details on who to contact should they have any concerns during their stay. We have had no instances of noise/bad behaviour since owning the property ', 'Guest_Access': 'There is a key safe beside the main door access to the flat that opens directly on to the street, Melbourne Road. Spare set keys are provided once inside the property. Should guests lose keys then another set is kept in North Berwick by Coast Properties', 'Access_Route': 'No properties overlook the flat. We are ground floor,  main door access, directly opposite Milsey Beach. We do have neighbouring flats either side of us & directly above. We are the only main door access property, to our knowledge, within the block of flats.\n', 'Parking_Facilities': 'Free on street parking directly outside flat & In neighbouring streets. Also within walking distance from car parks situated in North Berwick. The closest would be within 100m. This info is provided on the website Coast Properties & on booking ', 'Outdoor_Spaces': 'No outdoor space or storage facilities outwith the flat itself', 'Cleaning_Procedures': 'Guests are aware that the cleaning is maintained by CleanTec. Their contact details are provided within the “Breakwater Handbook” which is in the flat & easily accessible to read. Again these details are passed over on booking. When a booking is made the management company Coast Properties then pass details of length of booking directly to the cleaning team, CleanTec. These are then added to their own internal booking system to ensure smooth changeovers. Guests are asked to strip beds etc on leaving & to advise cleaning team if anything does not meet their standards on arrival. The cleaning team would then attend immediately to rectify should this be the case.', 'Complaints_Details': 'Any complaints would go, on first contact, to management company Coast Properties or CleanTec. Should the management company then require the owners to respond directly to the guests then we would be informed & would do so immediately.  Minor niggles, as with any holiday let, have been dealt with swiftly to guests satisfaction. Most recent issues  I can recall would be the key safe sticking when trying to access. This was rectified the same day by a maintenance team being on hand in North Berwick who supplied & installed a new key safe.'
        """,
"answer" :
        """
        Application Rewrite:
        Section: Description of the Property and Environment
        2.1.1. The property at hand is a culturally significant, main door accessible flat located at 17 Melbourne Road, North Berwick EH39 4JX. This flat, part of a residential stone block built around 1900, has historical importance and holds a reputable position within the city. The current proprietor, Julie Yvonne Hebdon, acquired it in August 2020.
        2.1.2. The flat, boasting one double bedroom and one twin bedroom, can comfortably host up to four guests. As a measure to maintain tranquility and uphold both the guests' and neighbors' comfort, the decision to exclude a sofa bed in the living area was intentionally made. This measure helps retain the property's residential character and prevents potential noise disruptions. Moreover, it underscores the property's purpose as a short-term guest accommodation, thereby preventing any changes that might affect its approved use.
        2.1.3. The main door, directly facing Melbourne Road, serves as the entrance to the property. A key box installed at the front door ensures the property's security. Inside the flat, next to the main door that faces Melbourne Road, there is a key safe. Extra sets of keys are provided inside the property, and if guests misplace their keys, another set is stored in North Berwick by Coast Properties.
        2.1.4. Free on-street parking is available directly outside the flat and along the surrounding streets. Additionally, the property is within walking distance to numerous car parks in North Berwick. This arrangement further substantiates the claim that the flat's usage as short-term guest accommodation minimally impacts the parking demand compared to long-term residential needs.
        """
  },
{
"query":
        """
        Great work. now do it again . create again with same input.  just checking it so i can assure you are generating right.
        """,
"answer" :
        """
        Absolutely, I understand. Here's the rewrite, strictly following the structure of the sample:
        Section: Property Profile and Environment
        2.1.1. The concerned property is an architecturally relevant flat located at 17 Melbourne Road, North Berwick EH39 4JX. It is an early 20th-century residential stone structure, forming part of a block of flats with historical and cultural importance within the city. The property was acquired by the current owner, Julie Yvonne Hebdon, in August 2020.
        2.1.2. The property internally comprises one double bedroom and one twin bedroom, providing accommodation for up to four guests. A deliberate decision has been made by the owner to exclude a sofa bed in the living room, aiming to maintain a serene atmosphere and prioritize the comfort of both guests and neighbors. This restriction on the number of occupants and the prevention of potential noise disturbances help retain the property's residential character. It also ensures the property's use aligns with short-term guest accommodation, mitigating potential changes that could affect its permitted use.
        2.1.3. The flat is directly accessible through the main door facing Melbourne Road. To secure the property, a key box has been installed by the front door. A key safe is available beside the main door inside the flat, also facing Melbourne Road. Additional keys are available within the property for use if needed. In an instance where the guests lose their keys, another set is kept in North Berwick by Coast Properties.
        2.1.4. Free on-street parking is available directly outside the flat and on nearby streets. Additionally, the property is ideally located within walking distance from various car parks in North Berwick. This arrangement further validates that the property's usage for short-term guest accommodation imposes minimal impact on parking demand compared to long-term residents.
        """

},
{
"query":
        """
        excellent work. please try not to write anything else other than just application. do not right any thing else
        great work now i will give you the input and do exactly as you did above
        'Time': Timestamp('2023-07-18 11:03:31.623000'), 'Contract_Number': 'ST1015', 'Full_Name': 'ruggero baietta', 'Email_Address': 'ruggerobaietta@gmail.com', 'Unique_Features': 'Our property is ground floor and opposite Medawbank shopping centre.', 'Property_Location': 'Ground floor, residential area but very close to a commercial one. Close to buses and a busy road, but extremely quiet and private at the same time. ', 'Proximity_to_POI': 'Holyrood Palace is less than 1 km away. ', 'Surroundings_Appeal': 'The property is very close to shops and restaurants, but at the same time it is nearby Holyrood Park and the pick of Arthur Seat. ', 'Occupancy_Rules': 'The property has got a dedicated parking spot. It is part of a building so we want to limit the maximum number of occupants to 4, having a double bedroom and a twin one. The large living room with a big sofa could easily accomodate more people, but to avoid parties and other noisy activities we do not allow more people to stay at the property. \nIt is a ground floor and there is only another flat at the same floor. The property is available all through the year and so far we did not have any complain from neighbours.', 'Minimum_Stay': '2 nights is the minimum stay and the average rental is probably 5 days but I need to investigate on this. I can easily send over the Airbnb bookings.', 'Guest_Screening': 'We take bookings from Airbnb mainly and we look at reviews of the guests.', 'House_Rules': 'No parties, no smoking and no noise that might disturb the neighbours.', 'Guest_Documentation': nan, 'Guest_Access': 'Main door of the building with keys, main door of the property again with keys. There is a self check-in with a lockbox located outside the property.', 'Access_Route': nan, 'Parking_Facilities': 'There is a dedicated parking spot and a p[hoto showing it to the guest', 'Outdoor_Spaces': 'There is a common garden in front of the property and a common area for rubbish bins.', 'Cleaning_Procedures': 'We have a cleaner going in after every guest. change of bed linens and towels and deep cleaning of all the property. For guests staying over a week we can provide extra cleaning/ changing of bed linen, towels. ', 'Complaints_Details': 'No complains so far'
        """,
"answer" :
        """
        Section: Property Overview and Surroundings
        2.1.1. The property under consideration is a noteworthy ground-floor flat located within a residential area, proximate to a commercial zone. The current owner, Ruggero Baietta, purchased the property on an unspecified date.
        2.1.2. The internal setup of the property includes a double bedroom and a twin bedroom, thus comfortably accommodating up to four guests. The owner has made a purposeful decision not to exceed this limit to prevent noisy activities such as parties. Despite having a large living room with a sizable sofa that could accommodate more individuals, this restriction helps preserve the tranquility of the building, which houses only one other flat on the same floor.
        2.1.3. Access to the building and the property is managed through a main door key. Additionally, a self-check-in feature is enabled by a lockbox located outside the property. In case of a key loss scenario, an undisclosed protocol is presumably in place to assist guests.
        2.1.4. The property comes with a dedicated parking spot for guest use, and a photograph is provided to guide guests to its location. The property's year-round availability and its limited capacity minimizes its impact on parking demand, ensuring the comfort of both guests and neighboring residents.
        """

},
{
"query":
        """
        Great now create for this:
        'Name': 'Philip John Myerscough', 'Full property address': 'Flat 2F1, 57 Merchiston Crescent, Edinburgh EH10 5AH', 'When did you commence trading as a short term let (approximately)': '01/2019. Ceased 09/2019. Long term let 09/2019 to 06/2020. Recommenced Autumn 2020', 'Number of bedrooms': 'The flat has 3 but we retain 1 and a store cupboard for our own use. So the flat is jet as 2 bedroom; max 4 people', 'Approximate size (sqm)': 'Total approx 135sqm Area let to tenants approx 120sqm', 'Property type (if flat describe floor, shared access, private entrance, etc)': "The flat is on the second floor. The stair serves 6 flats in total. 2 on first floor, 2 on second, 2 on third. The flat is the first on the second floor. The 2 ground floor flats in the building have their own front doors opening to the street. They each have an area of garden sheltering them from the street and the upper flats' entrance.", 'Can you provide a brief history of your ownership of property and description of the property and the area it is located in?': 'The property is a substantial 3 bedroom tenement flat constructed in 1890s in a sought after part of Edinburgh. It has views out over Edinburgh over the stone built villas opposite. Good public transport links. I bought the property in 2009 and substantially reformed it to create a modern, comfortable home for my family. I and my 2/3 children lived exclusively at the property until I retired. In mid 2018 we bought a house in Spain where we now live for most of the year.'
        """,
"answer" :
        """
        Section: Property Overview and Surroundings
        2.1.1. The property in question is a sizable, well-maintained flat located at Flat 2F1, 57 Merchiston Crescent, Edinburgh EH10 5AH. This 1890s-era tenement flat has been in the ownership of Philip John Myerscough since 2009 and has been transformed into a modern, comfortable dwelling.
        2.1.2. The flat comprises three bedrooms, but it is let as a two-bedroom accommodation to a maximum of four people, retaining one bedroom and a storage cupboard for the owner's personal use. The total area of the flat is approximately 135 square meters, with around 120 square meters allocated for guests.
        2.1.3. The property is situated on the second floor in a building that houses six flats in total. The stair serves all flats, with two each on the first, second, and third floors. The flat under consideration is the first one on the second floor. Two ground-floor flats in the building have private front doors and sheltered garden areas.
        2.1.4. The property is situated in a sought-after part of Edinburgh, with views overlooking the stone-built villas opposite. It enjoys good public transport links. The owner and their two to three children resided in the flat until the owner's retirement in 2018. Since then, the property has been periodically let as a short-term accommodation while the owner and their family reside in Spain for the majority of the year.
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
few_shot_prompt_2 = FewShotPromptTemplate(
    # These are the examples we want to insert into the prompt.
    examples=example_2,
    # This is how we want to format the examples when we insert them into the prompt.
    example_prompt=example_prompt,
    # The prefix is some text that goes before the examples in the prompt.
    # Usually, this consists of intructions.
    prefix = """
        ChatGPT, you are an application writer. Using the new applicant's details and following the structure and style of the original application, I need you to rewrite this application.
        You are an data entry and application writer for the Certificate of Lawful Use for Short-term Let Accommodation: Planning Statement.
        You will be given all the necessary information about the applicant in the input and your task is to follow a specific application format that will be provided and update that application text with the new information given to you as a text.
        Sample Section:
        Property Description and Surroundings
        2.1.1. The property in question is a historically significant flat situated at Breakwater, 17 Melbourne Road, North Berwick EH39 4JX. These flat houses carry cultural significance and are well-regarded within the city. The current owner of the property acquired it in September 2020.
        2.1.2. Inside the property, there is one double bedroom and one twin bedroom, allowing accommodation for up to four guests. The property owner has made a conscious decision not to include a sofa bed in the living room to maintain a peaceful environment and prioritize the comfort of both guests and neighbors. By limiting the number of occupants and avoiding potential noise disturbances, the residential character of the property is preserved. Additionally, this decision aligns with the property's intended use for short-term guest accommodation, rather than long-term residency, which helps avoid any changes that could affect its permitted use.
        2.1.3. The property can be accessed through the front door, which directly faces Melbourne Road. To secure the property, a key box has been installed at the front door. Inside the flat, there is a key safe beside the main door access, also facing Melbourne Road. Spare set keys are provided within the property. In case guests lose their keys, another set is kept in North Berwick by Coast Properties.
        2.1.4. There is free on-street parking available right outside the flat and in nearby streets. Furthermore, the property is conveniently located within walking distance from car parks situated in North Berwick. This preference further supports the argument that the property's use for short-term guest accommodation has a minimal impact on parking demand compared to the requirements of long-term residents
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