
from langchain import PromptTemplate, FewShotPromptTemplate



### few short learning examples for gpt

example_3 =[
{"query":"""
        Dear GPT,
        I need your help in rewriting an application for a new applicant. Please follow the exact structure and style of the template application below
        kindly please do not generate anything else only the application. Your are restricted to generate line numbering exactly as in the template application. which are 5.1.1 to 5.1.16.
        template Application:
        5.	Assessment
        5.1.1.	As Lord Justice Sullivan noted in his ruling, the Planning Authority is ‘entitled’ to form a view as to whether a material change of use has taken place; based on matters of fact and degree.
        5.1.2.	Turning to the subject property at Flat 6, 77 Cumberland Street, (address change here) as already noted, the 2021 Guidance document referred to in section 4 of this Planning Statement provides a useful list of relevant matters that will allow the fact and degree of any change from a residential use to a short term let use to be assessed.
        5.1.3.	To assist the Planning Authority in its assessment of these matters, the paragraphs that follow offers some consideration of the subject property when assessed against these matters.
        The character of the new use and of the wider area
        5.1.4.	The short term let use allows visitors to the city to stay temporarily in residential properties. Very often such stays are marketed as allowing visitors to ‘live like locals’. The emphasis of such use is on visitors behaving in such a way that they feel like they are permanent residents. In this way, guests that want to give most expression to the idea of living like a local will act and behave in a manner that is practically indistinguishable from that of a permanent resident.
        5.1.5.	In terms of the character of the wider area, the property is located in Edinburgh’s New Town (town info may change). This is an explicitly urban quarter of the city, expressly laid out as such in the late 18th century and early 19th Century. In such areas, acting reasonably, both permanent residents and visitors should recognise that an urban setting like this can absorb a relatively wide range of urban activities. These might include: people coming in and out of buildings at different times of day and night; people and vehicles moving along streets at different times of day and night; and, commercial activity taking place predominantly during the day.
        5.1.6.	The property at 77 Cumberland Street (address and measurement and town info change) is located less than 50 metres from a public house with a beer garden, and less than 200 metres from an area beginning on St Stephen’s Street designated in City of Edinburgh Council’s Adopted Local Development Plan 2016 as performing a ‘town centre’ function for Stockbridge.
        5.1.7.	Overall, the immediate area surrounding the property is considered to be relatively busy where some activity is reasonably to be expected. It is considered that for many people the ongoing activity that the area supports would be regarded as a benefit rather than as an adverse outcome; and compares favourably with perhaps the vast majority of places elsewhere in Scotland where such activity does not occur. The latent activity levels that this area enjoys also means that this is an area that has shown itself capable of assimilating a range of uses together in a host urban environment that does not appear to be fragile or adversely sensitive to change.
        The size of the property
        5.1.8.	(change bedroom and max people and measurement info) The property has one double-bedroom. It is advertised as capable of hosting a maximum of 3 people. The property extends to approximately 44 sqm. This is considerably smaller than the 52sqm minimum standard for a one-bedroom residential property identified by the City of Edinburgh Council in its January 2020 Design Guidance document. The reason stated in the document for defining these minimum space standards was ‘in order to ensure satisfactory amenity’.
        5.1.9.	(change bedroom and resident count and visitor info) For the avoidance of doubt, a one-bedroom property like this would be equally capable of hosting either 3 permanent residents (a couple and a child) or 3 visitors (a couple and a child).
        The pattern of activity associated with the use including numbers of occupants, the period of use, issues of noise, disturbance and parking demand
        5.1.10.	(change guest count info) As noted above, the maximum number of guests that could stay in the property would be 3. The applicant has confirmed that a minimum stay duration of (change amount of nights and month info) 2 nights is in place throughout most of the year, with this total rising to a 4 night minimum stay in August. The applicant advises that the property is used as a short term let an average of 9 nights per calendar month.
        5.1.11.	Each guest is vetted by the hosting company that looks after its servicing. Under its own procedures, the company ensures that no-one under the age of 25 is allowed to rent the property.
        5.1.12.	All guests are required to agree to ‘house rules’ for the property at the point of booking. These rules outlaw practices such as: smoking or vaping anywhere in the property; holding parties; and keeping pets. The guest book provided with the property for each group of guests explains these rules as well as providing further detail on matters such as refuse disposal and recycling; bag storage and nearby parking; and ‘quiet periods’ in the property (between 10pm and 7.30am) (hours may change).
        5.1.13.	To assist in assessing the property against this matter, a copy of the property’s guest book as well as a copy of the hosting company’s house rules have been appended to this application as supporting documents. Overall, it is considered that there is far greater control of guest behaviour and of all activity that can take place in the property than would be the case if it was let out to a permanent resident.
        The nature and character of any services provided
        5.1.14.	For those arriving by car, guests are directed to suggested local public car parks within the guest book provided with the property. For the avoidance of doubt, the lack of car parking is made clear on the property’s online listing. Anecdotally, the hosting company has confirmed that most guests in fact arrive by train or plane and do not require parking of any description.
        5.1.15.	The property has no access to any private or shared outside amenity garden areas. (storage rules may change here) It also has no bag storage facilities on site (although again, suggested commercial outlets where bag storage is available is detailed in the guest book).
        5.1.16.	All cleaning of the property takes place after check-out/departures (10.30 am) (times listed here may change) and before check-in/arrivals (4pm). Accordingly, the servicing of the property always takes place in office hours and not during anti- social times.
        Also about the above query, the text inside the round brackets is for your understanding, you must not include this when you are re writing the application text as per above format exactly.
        must not reply with any other answer.you must only asnwer with the regenerated same pattern application from the input information given to you.
        The information for the new applicant is as follows:
        'Time': Timestamp('2023-07-18 11:03:31.623000'),'Contract_Number#': 'ST1012', 'Full_Name': 'Julie Yvonne Hebdon', 'Email_Address': 'juleshebdon65@gmail.com', 'Unique_Features': ' Main door accessible flat directly onto Melbourne Road', 'Property_Location': '17 Melbourne Road, North Berwick EH39 4JX. Part of a residential stone,  built approx 1900,  block of flats. We are ground floor main door access, directly opposite Milsey Beach in North Berwick. There are no properties overlooking the flat. The surrounding properties are a mix of residential & holiday let’s. The flat is within walking distance to beach less than  50m  & shops/restaurants less than 500m from the property.', 'Proximity_to_POI': 'Coastal Communities Museum 100m. Scottish Seabird Centre 100m.', 'Surroundings_Appeal': 'The property is directly opposite Milsey Beach. This appeals to guests & its proximity to shops/restaurants of North Berwick. Easy access to train station/bus links makes travel available to all that visit. Free on street parking outside the flat also.', 'Occupancy_Rules': 'Maximum occupancy 4. No hen or stag parties permitted. Free on street parking directly outside the flat & in neighbouring streets but also within close proximity to car parks that are within walking distance. No guests have ever complained of lack of parking. Period of use varies with individual bookings, from long weekends to fortnight bookings. Out of season minimum night stay is usually 3 nights whilst in high season this will be 7 nights. We accommodate predominantly families or couples & also allow 2 small dogs. We have never had any issues of disturbance/noise with any of the guests that have stayed or from residents neighbouring our property. Our management company Coast Properties would be able to verify that no complaints have been received regarding the issues stated above.', 'Minimum_Stay': '3 nights in low season. 7 nights in high season. Coast Properties, the management company for Breakwater have provided 10 year continuous holiday let information together with bookings for the last financial year to support this application. We purchased the property in August 2020. At this time this property formally called Aviemore was marketed by Coast Properties & had been so for the previous 10 years. We have maintained this relationship, keeping the marketing of Breakwater (formally Aviemore) from purchase to date.', 'Guest_Screening': 'No hen or stag parties permitted with a max of 2 dogs allowed. Guest screening/vetting is completed by our management company Coast Properties. Predominantly our bookings are repeat business from guests from one year to the next. We have never experienced any guest being declined a booking or future booking but this is covered within T&Cs of booking with Coast Properties.', 'House_Rules': 'There is a guest “Breakwater Handbook” communicating all info regarding their booking. All that the guest may require from contact info for Coast Properties, the cleaning team CleanTec, contact information for emergencies be that police/fire or hospital details. An insight into the local area & what they can expect from their visit re attractions/sights of interest. There is also in situ a “Breakwater Appliance Guide” detailing all they need to know & how the heating/water works etc. Also in situ is a  “Breakwater Important Info” this includes EPC, Legionella Certificate of Compliance, PAT Report/Certificate, EICR, Fire Risk Assessment Report. All these are up to date & there are procedures in place to ensure that they remain so. Guests have peace of mind that their safety during their stay is considered with regular maintenance of both smoke detectors, fire extinguisher & first aid kit regularly carried out. This can also be evidenced.', 'Guest_Documentation': 'In situ “Breakwater Handbook” gives guests details on who to contact should they have any concerns during their stay. We have had no instances of noise/bad behaviour since owning the property ', 'Guest_Access': 'There is a key safe beside the main door access to the flat that opens directly on to the street, Melbourne Road. Spare set keys are provided once inside the property. Should guests lose keys then another set is kept in North Berwick by Coast Properties', 'Access_Route': 'No properties overlook the flat. We are ground floor,  main door access, directly opposite Milsey Beach. We do have neighbouring flats either side of us & directly above. We are the only main door access property, to our knowledge, within the block of flats.\n', 'Parking_Facilities': 'Free on street parking directly outside flat & In neighbouring streets. Also within walking distance from car parks situated in North Berwick. The closest would be within 100m. This info is provided on the website Coast Properties & on booking ', 'Outdoor_Spaces': 'No outdoor space or storage facilities outwith the flat itself', 'Cleaning_Procedures': 'Guests are aware that the cleaning is maintained by CleanTec. Their contact details are provided within the “Breakwater Handbook” which is in the flat & easily accessible to read. Again these details are passed over on booking. When a booking is made the management company Coast Properties then pass details of length of booking directly to the cleaning team, CleanTec. These are then added to their own internal booking system to ensure smooth changeovers. Guests are asked to strip beds etc on leaving & to advise cleaning team if anything does not meet their standards on arrival. The cleaning team would then attend immediately to rectify should this be the case.', 'Complaints_Details': 'Any complaints would go, on first contact, to management company Coast Properties or CleanTec. Should the management company then require the owners to respond directly to the guests then we would be informed & would do so immediately.  Minor niggles, as with any holiday let, have been dealt with swiftly to guests satisfaction. Most recent issues  I can recall would be the key safe sticking when trying to access. This was rectified the same day by a maintenance team being on hand in North Berwick who supplied & installed a new key safe.'
        Could you please generate the rewritten application?
         """,
 "answer":
        """
        Assessment
        5.1.1. Building upon Lord Justice Sullivan's judgment, it is within the Planning Authority's rights to ascertain if there has been a material change of use, rooted in factual and degree-based analysis.
        5.1.2. With a focus on the property located at 17 Melbourne Road, North Berwick EH39 4JX, it is worth mentioning that the 2021 Guidance document discussed in section 4 of this Planning Statement provides an extensive inventory of pertinent factors that will facilitate the assessment of any shift from a residential to a short term let use.
        5.1.3. In order to support the Planning Authority in evaluating these elements, the subsequent sections provide an appraisal of the property in question against these considerations.
        The character of the new use and of the wider area
        5.1.4. The short-term let use offers city visitors a temporary residence. Typically, these stays are promoted as an opportunity to 'live like locals', encouraging visitors to adopt behaviours of permanent residents, thereby making it difficult to distinguish between the two.
        5.1.5. Regarding the broader area's character, the property is situated in North Berwick's residential district, a mixed-use area comprising both residential properties and holiday lets. Given its urban setting, residents and visitors are expected to understand that a diverse range of activities, including various patterns of human and vehicular movement and commercial activities, is part of urban living.
        5.1.6. The property at 17 Melbourne Road is positioned less than 50 metres from Milsey Beach and within 500 metres of a vibrant shopping and dining area, thereby serving a central function for North Berwick.
        5.1.7. Overall, the immediate vicinity of the property is considered bustling, indicating that a certain level of activity is reasonably anticipated. This active environment could be viewed as a positive aspect rather than a detriment, comparing favourably to many places in Scotland where such vibrant activity is absent. The inherent liveliness of this area also demonstrates its capability to accommodate a variety of uses within a robust and resilient urban setting.
        The size of the property
        5.1.8. The property comprises a double-bedroom, suitable for hosting up to four individuals, and measures approximately 44 sqm. This size falls significantly below the 52sqm minimum standard set by the City of Edinburgh Council in its 2020 Design Guidance document, which was established to guarantee satisfactory living conditions.
        5.1.9. For clarity, a one-bedroom property like this is equally suitable for hosting either four permanent residents (for instance, a couple with two children) or four visitors (for instance, two couples).
        The pattern of activity associated with the use including numbers of occupants, the period of use, issues of noise, disturbance and parking demand
        5.1.10. As mentioned earlier, the property can accommodate up to four guests. The applicant has affirmed that the property's minimum stay duration is 3 nights during low season, extending to 7 nights during high season. On average, the property is rented short term for 9 nights per calendar month.
        5.1.11. Each guest is screened by Coast Properties, the management company responsible for servicing the property. According to their procedures, individuals under 25 are not allowed to rent the property.
        5.1.12. Guests must agree to the property's 'house rules' at the point of booking, prohibiting activities such as smoking or vaping, parties, and pets. The guest handbook provided further explains these rules, detailing additional requirements related to refuse disposal and recycling, bag storage, nearby parking, and quiet hours (from 10pm to 7.30am).
        5.1.13. To aid in evaluating the property against these criteria, a copy of the property's guest handbook and the management company's house rules have been appended to this application. It is noteworthy that there are stricter controls over guest behaviour and activities compared to a permanent resident scenario.
        The nature and character of any services provided
        5.1.14. Guests arriving by car are directed to local public car parks listed in the guest handbook. It is clearly stated in the property's online listing that there is no dedicated parking. The management company reports that the majority of guests arrive by train or plane, thus not requiring parking.
        5.1.15. The property lacks access to any private or shared outdoor spaces or on-site bag storage facilities (though commercial outlets providing bag storage are mentioned in the guest handbook).
        5.1.16. Cleaning of the property is scheduled after check-out/departures (10.30 am) and before check-in/arrivals (4pm), ensuring property servicing occurs during standard business hours and not during quiet periods.
        """
},
{"query":
 """
        excellent work.
        great work now i will give you the input to check if you are generating okay.
        'Time': Timestamp('2023-07-18 11:03:31.623000'), 'Contract_Number': 'ST1015', 'Full_Name': 'ruggero baietta', 'Email_Address': 'ruggerobaietta@gmail.com', 'Unique_Features': 'Our property is ground floor and opposite Medawbank shopping centre.', 'Property_Location': 'Ground floor, residential area but very close to a commercial one. Close to buses and a busy road, but extremely quiet and private at the same time. ', 'Proximity_to_POI': 'Holyrood Palace is less than 1 km away. ', 'Surroundings_Appeal': 'The property is very close to shops and restaurants, but at the same time it is nearby Holyrood Park and the pick of Arthur Seat. ', 'Occupancy_Rules': 'The property has got a dedicated parking spot. It is part of a building so we want to limit the maximum number of occupants to 4, having a double bedroom and a twin one. The large living room with a big sofa could easily accomodate more people, but to avoid parties and other noisy activities we do not allow more people to stay at the property. \nIt is a ground floor and there is only another flat at the same floor. The property is available all through the year and so far we did not have any complain from neighbours.', 'Minimum_Stay': '2 nights is the minimum stay and the average rental is probably 5 days but I need to investigate on this. I can easily send over the Airbnb bookings.', 'Guest_Screening': 'We take bookings from Airbnb mainly and we look at reviews of the guests.', 'House_Rules': 'No parties, no smoking and no noise that might disturb the neighbours.', 'Guest_Documentation': nan, 'Guest_Access': 'Main door of the building with keys, main door of the property again with keys. There is a self check-in with a lockbox located outside the property.', 'Access_Route': nan, 'Parking_Facilities': 'There is a dedicated parking spot and a p[hoto showing it to the guest', 'Outdoor_Spaces': 'There is a common garden in front of the property and a common area for rubbish bins.', 'Cleaning_Procedures': 'We have a cleaner going in after every guest. change of bed linens and towels and deep cleaning of all the property. For guests staying over a week we can provide extra cleaning/ changing of bed linen, towels. ', 'Complaints_Details': 'No complains so far'
         """,
 "answer":
        """

        Sure, here is the desired JSON format for the input data:
        
            "Time": "2023-07-18T11:03:31.623Z",
            "Contract_Number": "ST1015",
            "Full_Name": "ruggero baietta",
            "Email_Address": "ruggerobaietta@gmail.com",
            "Unique_Features": "Our property is ground floor and opposite Medawbank shopping centre.",
            "Property_Location": "Ground floor, residential area but very close to a commercial one. Close to buses and a busy road, but extremely quiet and private at the same time.",
            "Proximity_to_POI": "Holyrood Palace is less than 1 km away.",
            "Surroundings_Appeal": "The property is very close to shops and restaurants, but at the same time it is nearby Holyrood Park and the pick of Arthur Seat.",
            "Occupancy_Rules": "The property has got a dedicated parking spot. It is part of a building so we want to limit the maximum number of occupants to 4, having a double bedroom and a twin one. The large living room with a big sofa could easily accomodate more people, but to avoid parties and other noisy activities we do not allow more people to stay at the property.\nIt is a ground floor and there is only another flat at the same floor. The property is available all through the year and so far we did not have any complain from neighbours.",
            "Minimum_Stay": "2 nights is the minimum stay and the average rental is probably 5 days but I need to investigate on this. I can easily send over the Airbnb bookings.",
            "Guest_Screening": "We take bookings from Airbnb mainly and we look at reviews of the guests.",
            "House_Rules": "No parties, no smoking and no noise that might disturb the neighbours.",
            "Guest_Documentation": null,
            "Guest_Access": "Main door of the building with keys, main door of the property again with keys. There is a self check-in with a lockbox located outside the property.",
            "Access_Route": null,
            "Parking_Facilities": "There is a dedicated parking spot and a p[hoto showing it to the guest",
            "Outdoor_Spaces": "There is a common garden in front of the property and a common area for rubbish bins.",
            "Cleaning_Procedures": "We have a cleaner going in after every guest. change of bed linens and towels and deep cleaning of all the property. For guests staying over a week we can provide extra cleaning/ changing of bed linen, towels.",
            "Complaints_Details": "No complains so far"
        

        """
},
{"query":
        """
        great work now i will give you the input and do exactly as you did above
        'Time': Timestamp('2023-07-18 11:03:31.623000'), 'Contract_Number': 'ST1015', 'Full_Name': 'ruggero baietta', 'Email_Address': 'ruggerobaietta@gmail.com', 'Unique_Features': 'Our property is ground floor and opposite Medawbank shopping centre.', 'Property_Location': 'Ground floor, residential area but very close to a commercial one. Close to buses and a busy road, but extremely quiet and private at the same time. ', 'Proximity_to_POI': 'Holyrood Palace is less than 1 km away. ', 'Surroundings_Appeal': 'The property is very close to shops and restaurants, but at the same time it is nearby Holyrood Park and the pick of Arthur Seat. ', 'Occupancy_Rules': 'The property has got a dedicated parking spot. It is part of a building so we want to limit the maximum number of occupants to 4, having a double bedroom and a twin one. The large living room with a big sofa could easily accomodate more people, but to avoid parties and other noisy activities we do not allow more people to stay at the property. \nIt is a ground floor and there is only another flat at the same floor. The property is available all through the year and so far we did not have any complain from neighbours.', 'Minimum_Stay': '2 nights is the minimum stay and the average rental is probably 5 days but I need to investigate on this. I can easily send over the Airbnb bookings.', 'Guest_Screening': 'We take bookings from Airbnb mainly and we look at reviews of the guests.', 'House_Rules': 'No parties, no smoking and no noise that might disturb the neighbours.', 'Guest_Documentation': nan, 'Guest_Access': 'Main door of the building with keys, main door of the property again with keys. There is a self check-in with a lockbox located outside the property.', 'Access_Route': nan, 'Parking_Facilities': 'There is a dedicated parking spot and a p[hoto showing it to the guest', 'Outdoor_Spaces': 'There is a common garden in front of the property and a common area for rubbish bins.', 'Cleaning_Procedures': 'We have a cleaner going in after every guest. change of bed linens and towels and deep cleaning of all the property. For guests staying over a week we can provide extra cleaning/ changing of bed linen, towels. ', 'Complaints_Details': 'No complains so far'
        """,
 "answer":
        """
        Dear Housing Application Review Board,
        Please kindly find the submitted details for a new application from Mr. Ruggero Baietta, contract number ST1015, on the 18th of July, 2023 at 11:03:31.623000.
        The property that Mr. Baietta manages is conveniently situated on the ground floor and is uniquely positioned opposite the Medawbank shopping centre. This advantageous location combines the tranquility of a residential neighborhood with the vibrancy of commercial activity. Despite its close proximity to public transport and a busy road, the property maintains a serene, private atmosphere.
        Notably, the property boasts an outstanding location less than a kilometer from Holyrood Palace. Its immediate surroundings feature an appealing blend of retail shops, dining establishments, and natural attractions such as Holyrood Park and Arthur Seat.
        The property comes with its own dedicated parking spot and has a maximum occupancy of four. It is composed of a double and a twin bedroom. The spacious living room could potentially accommodate more guests, but in order to maintain a respectful, noise-free environment, additional occupancy is discouraged. The property is part of a duplex and is available for rent year-round, without any previous complaints from neighbors.
        Guests are required to stay for a minimum of two nights, with an average rental duration of around five days. Booking is mainly done through Airbnb, with potential guests vetted through their review system. House rules are straightforward: no parties, smoking, or noise that could disturb the neighbors.
        Guests will have access to the main building and property using keys, with a lockbox provided for self check-in. The property also includes a dedicated parking spot which is visibly marked and photographed for guests. Outdoor spaces include a common garden and a trash bin area.
        A professional cleaner ensures the property remains spotless, providing fresh bed linens and towels, and a deep clean after every guest. Longer-staying guests can avail of additional cleaning services.
        To date, Mr. Baietta is pleased to report no complaints regarding the property.
        We hope you find all the information provided satisfactory and look forward to your favorable response.
        Best Regards,[Your Name]
        """
},
{
 "query":
        """
        please only follow the instructions
        please donot write supporting information and other sections only the required

        """,
 "answer":
        """
        Sure, here is the desired JSON format for the input data:
        "Time": "2023-07-18T11:03:31.623Z",
        "Contract_Number": "ST1015",
        "Full_Name": "ruggero baietta",
        "Email_Address": "ruggerobaietta@gmail.com",
        "Unique_Features": "Our property is ground floor and opposite Medawbank shopping centre.",
        "Property_Location": "Ground floor, residential area but very close to a commercial one. Close to buses and a busy road, but extremely quiet and private at the same time.",
        "Proximity_to_POI": "Holyrood Palace is less than 1 km away.",
        "Surroundings_Appeal": "The property is very close to shops and restaurants, but at the same time it is nearby Holyrood Park and the pick of Arthur Seat.",
        "Occupancy_Rules": "The property has got a dedicated parking spot. It is part of a building so we want to limit the maximum number of occupants to 4, having a double bedroom and a twin one. The large living room with a big sofa could easily accomodate more people, but to avoid parties and other noisy activities we do not allow more people to stay at the property.\nIt is a ground floor and there is only another flat at the same floor. The property is available all through the year and so far we did not have any complain from neighbours.",
        "Minimum_Stay": "2 nights is the minimum stay and the average rental is probably 5 days but I need to investigate on this. I can easily send over the Airbnb bookings.",
        "Guest_Screening": "We take bookings from Airbnb mainly and we look at reviews of the guests.",
        "House_Rules": "No parties, no smoking and no noise that might disturb the neighbours.",
        "Guest_Documentation": null,
        "Guest_Access": "Main door of the building with keys, main door of the property again with keys. There is a self check-in with a lockbox located outside the property.",
        "Access_Route": null,
        "Parking_Facilities": "There is a dedicated parking spot and a p[hoto showing it to the guest",
        "Outdoor_Spaces": "There is a common garden in front of the property and a common area for rubbish bins.",
        "Cleaning_Procedures": "We have a cleaner going in after every guest. change of bed linens and towels and deep cleaning of all the property. For guests staying over a week we can provide extra cleaning/ changing of bed linen, towels.",
        "Complaints_Details": "No complains so far"
        
        """

},
{
"query":
        """
        Dear GPT,
        I need your help in rewriting an application for a new applicant. Please follow the the instruction i gave yo
        """,
"answer":
        """
        Of course! Please provide the information or content that needs to be rewritten, along with any specific instructions or style guidelines you would like me to follow. I'm here to help
        """
} , 
{
"query":
        """
        excellent work.
        great work now i will give you the input and do exactly as you did above
        'Time': Timestamp('2023-07-18 11:03:31.623000'), 'Contract_Number': 'ST1015', 'Full_Name': 'ruggero baietta', 'Email_Address': 'ruggerobaietta@gmail.com', 'Unique_Features': 'Our property is ground floor and opposite Medawbank shopping centre.', 'Property_Location': 'Ground floor, residential area but very close to a commercial one. Close to buses and a busy road, but extremely quiet and private at the same time. ', 'Proximity_to_POI': 'Holyrood Palace is less than 1 km away. ', 'Surroundings_Appeal': 'The property is very close to shops and restaurants, but at the same time it is nearby Holyrood Park and the pick of Arthur Seat. ', 'Occupancy_Rules': 'The property has got a dedicated parking spot. It is part of a building so we want to limit the maximum number of occupants to 4, having a double bedroom and a twin one. The large living room with a big sofa could easily accomodate more people, but to avoid parties and other noisy activities we do not allow more people to stay at the property. \nIt is a ground floor and there is only another flat at the same floor. The property is available all through the year and so far we did not have any complain from neighbours.', 'Minimum_Stay': '2 nights is the minimum stay and the average rental is probably 5 days but I need to investigate on this. I can easily send over the Airbnb bookings.', 'Guest_Screening': 'We take bookings from Airbnb mainly and we look at reviews of the guests.', 'House_Rules': 'No parties, no smoking and no noise that might disturb the neighbours.', 'Guest_Documentation': nan, 'Guest_Access': 'Main door of the building with keys, main door of the property again with keys. There is a self check-in with a lockbox located outside the property.', 'Access_Route': nan, 'Parking_Facilities': 'There is a dedicated parking spot and a p[hoto showing it to the guest', 'Outdoor_Spaces': 'There is a common garden in front of the property and a common area for rubbish bins.', 'Cleaning_Procedures': 'We have a cleaner going in after every guest. change of bed linens and towels and deep cleaning of all the property. For guests staying over a week we can provide extra cleaning/ changing of bed linen, towels. ', 'Complaints_Details': 'No complains so far'
        """,
"answer":
        """
        Dear Housing Application Review Board,
        Please kindly find the submitted details for a new application from Mr. Ruggero Baietta, contract number ST1015, on the 18th of July, 2023 at 11:03:31.623000.
        The property that Mr. Baietta manages is conveniently situated on the ground floor and is uniquely positioned opposite the Medawbank shopping centre. This advantageous location combines the tranquility of a residential neighborhood with the vibrancy of commercial activity. Despite its close proximity to public transport and a busy road, the property maintains a serene, private atmosphere.
        Notably, the property boasts an outstanding location less than a kilometer from Holyrood Palace. Its immediate surroundings feature an appealing blend of retail shops, dining establishments, and natural attractions such as Holyrood Park and Arthur Seat.
        The property comes with its own dedicated parking spot and has a maximum occupancy of four. It is composed of a double and a twin bedroom. The spacious living room could potentially accommodate more guests, but in order to maintain a respectful, noise-free environment, additional occupancy is discouraged. The property is part of a duplex and is available for rent year-round, without any previous complaints from neighbors.
        Guests are required to stay for a minimum of two nights, with an average rental duration of around five days. Booking is mainly done through Airbnb, with potential guests vetted through their review system. House rules are straightforward: no parties, smoking, or noise that could disturb the neighbors.
        Guests will have access to the main building and property using keys, with a lockbox provided for self check-in. The property also includes a dedicated parking spot which is visibly marked and photographed for guests. Outdoor spaces include a common garden and a trash bin area.
        A professional cleaner ensures the property remains spotless, providing fresh bed linens and towels, and a deep clean after every guest. Longer-staying guests can avail of additional cleaning services.
        To date, Mr. Baietta is pleased to report no complaints regarding the property.
        We hope you find all the information provided satisfactory and look forward to your favorable response.
        Best Regards,
        Your Name
        """
} , 
{
"query":
         """
        please only follow the instructions
        please donot write supporting information and other sections only the required
         """,
"answer":
        """
        Dear Housing Application Review Board,
        This application pertains to Mr. Ruggero Baietta, holding Contract_Number: ST1015, dated 2023-07-18 11:03:31.623000. You may reach him at ruggerobaietta@gmail.com for any further communication.
        The property under application is a ground floor property, distinctively situated opposite the Medawbank shopping centre. Its location is an intriguing balance of residential calm and commercial buzz, offering tranquility and convenience simultaneously. A remarkable point of interest, Holyrood Palace, is less than a kilometer away, adding to the property's attractiveness.
        The property is part of a building, limiting occupancy to a maximum of four people, and includes a double and a twin bedroom. Despite the capacious living room, the number of occupants is limited to ensure noise-free premises. A noteworthy feature of the property is its dedicated parking spot.
        The minimum stay policy at the property is two nights, with the average rental duration being approximately five days. Bookings are primarily handled via Airbnb, with guests screened based on their reviews. The property enforces straightforward house rules: no parties, smoking, or noise that may disturb neighbours.
        Guests will be provided keys to the main door of the building and property, and self-check-in is facilitated with a lockbox located outside the property. The property comes with a dedicated parking spot and outdoor spaces include a common garden and a trash bin area.
        After every guest's stay, a professional cleaner ensures a thorough cleaning of the property, change of bed linens and towels, and provision for additional cleaning services for guests staying over a week.
        The property proudly stands with a clean record of no complaints to date.
        Kind Regards,
        Your Name
        """    
},
{
"query":
         """
        Dear GPT,
        I need your help in rewriting an application for a new applicant. Please follow the exact structure and style of the sample application below
        kindly please do not generate anything else only the application
        Sample Section:
        5.	Assessment
        5.1.1.	As Lord Justice Sullivan noted in his ruling, the Planning Authority is ‘entitled’ to form a view as to whether a material change of use has taken place; based on matters of fact and degree.
        5.1.2.	Turning to the subject property at Flat 6, 77 Cumberland Street, (address change here) as already noted, the 2021 Guidance document referred to in section 4 of this Planning Statement provides a useful list of relevant matters that will allow the fact and degree of any change from a residential use to a short term let use to be assessed.
        5.1.3.	To assist the Planning Authority in its assessment of these matters, the paragraphs that follow offers some consideration of the subject property when assessed against these matters.
        The character of the new use and of the wider area
        5.1.4.	The short term let use allows visitors to the city to stay temporarily in residential properties. Very often such stays are marketed as allowing visitors to ‘live like locals’. The emphasis of such use is on visitors behaving in such a way that they feel like they are permanent residents. In this way, guests that want to give most expression to the idea of living like a local will act and behave in a manner that is practically indistinguishable from that of a permanent resident.
        5.1.5.	In terms of the character of the wider area, the property is located in Edinburgh’s New Town (town info may change). This is an explicitly urban quarter of the city, expressly laid out as such in the late 18th century and early 19th Century. In such areas, acting reasonably, both permanent residents and visitors should recognise that an urban setting like this can absorb a relatively wide range of urban activities. These might include: people coming in and out of buildings at different times of day and night; people and vehicles moving along streets at different times of day and night; and, commercial activity taking place predominantly during the day.
        5.1.6.	The property at 77 Cumberland Street (address and measurement and town info change) is located less than 50 metres from a public house with a beer garden, and less than 200 metres from an area beginning on St Stephen’s Street designated in City of Edinburgh Council’s Adopted Local Development Plan 2016 as performing a ‘town centre’ function for Stockbridge.
        5.1.7.	Overall, the immediate area surrounding the property is considered to be relatively busy where some activity is reasonably to be expected. It is considered that for many people the ongoing activity that the area supports would be regarded as a benefit rather than as an adverse outcome; and compares favourably with perhaps the vast majority of places elsewhere in Scotland where such activity does not occur. The latent activity levels that this area enjoys also means that this is an area that has shown itself capable of assimilating a range of uses together in a host urban environment that does not appear to be fragile or adversely sensitive to change.
        The size of the property
        5.1.8.	(change bedroom and max people and measurement info) The property has one double-bedroom. It is advertised as capable of hosting a maximum of 3 people. The property extends to approximately 44 sqm. This is considerably smaller than the 52sqm minimum standard for a one-bedroom residential property identified by the City of Edinburgh Council in its January 2020 Design Guidance document. The reason stated in the document for defining these minimum space standards was ‘in order to ensure satisfactory amenity’.
        5.1.9.	(change bedroom and resident count and visitor info) For the avoidance of doubt, a one-bedroom property like this would be equally capable of hosting either 3 permanent residents (a couple and a child) or 3 visitors (a couple and a child).
        The pattern of activity associated with the use including numbers of occupants, the period of use, issues of noise, disturbance and parking demand
        5.1.10.	(change guest count info) As noted above, the maximum number of guests that could stay in the property would be 3. The applicant has confirmed that a minimum stay duration of (change amount of nights and month info) 2 nights is in place throughout most of the year, with this total rising to a 4 night minimum stay in August. The applicant advises that the property is used as a short term let an average of 9 nights per calendar month.
        5.1.11.	Each guest is vetted by the hosting company that looks after its servicing. Under its own procedures, the company ensures that no-one under the age of 25 is allowed to rent the property.
        5.1.12.	All guests are required to agree to ‘house rules’ for the property at the point of booking. These rules outlaw practices such as: smoking or vaping anywhere in the property; holding parties; and keeping pets. The guest book provided with the property for each group of guests explains these rules as well as providing further detail on matters such as refuse disposal and recycling; bag storage and nearby parking; and ‘quiet periods’ in the property (between 10pm and 7.30am) (hours may change).
        5.1.13.	To assist in assessing the property against this matter, a copy of the property’s guest book as well as a copy of the hosting company’s house rules have been appended to this application as supporting documents. Overall, it is considered that there is far greater control of guest behaviour and of all activity that can take place in the property than would be the case if it was let out to a permanent resident.
        The nature and character of any services provided
        5.1.14.	For those arriving by car, guests are directed to suggested local public car parks within the guest book provided with the property. For the avoidance of doubt, the lack of car parking is made clear on the property’s online listing. Anecdotally, the hosting company has confirmed that most guests in fact arrive by train or plane and do not require parking of any description.
        5.1.15.	The property has no access to any private or shared outside amenity garden areas. (storage rules may change here) It also has no bag storage facilities on site (although again, suggested commercial outlets where bag storage is available is detailed in the guest book).
        5.1.16.	All cleaning of the property takes place after check-out/departures (10.30 am) (times listed here may change) and before check-in/arrivals (4pm). Accordingly, the servicing of the property always takes place in office hours and not during anti- social times.
         """,
"answer":
        """
        Assessment
        5.1.1. As articulated by Lord Justice Sullivan, the Planning Authority is 'entitled' to form a perspective on whether a material change of use has transpired, based on facts and degree.
        5.1.2. Turning our attention to the proposed property at Ground Floor, Medawbank Shopping Centre, (address change here) as mentioned before, the 2021 Guidance document mentioned in section 4 of this Planning Statement provides a comprehensive list of relevant aspects that will enable the assessment of the extent and fact of any change from a residential use to a short-term let use.
        5.1.3. The subsequent paragraphs intend to assist the Planning Authority in its evaluation of these aspects, considering the proposed property against these factors.
        The Character of the New Use and of the Wider Area
        5.1.4. The short-term let use permits city visitors to temporarily inhabit residential properties. Marketed as 'living like locals', such stays emphasise the idea of guests conducting themselves as though they are permanent residents. As a result, guests who value this concept will behave in a way virtually indistinguishable from permanent residents.
        5.1.5. Concerning the character of the broader area, the property is nestled in Edinburgh's New Town (town info may change), a distinctively urban quarter of the city, established as such in the late 18th and early 19th centuries. Reasonably, both permanent residents and visitors should recognize that an urban setting like this can accommodate a relatively broad range of urban activities. This includes different times of movement for people and vehicles, and daytime commercial activity.
        5.1.6. The property at Medawbank Shopping Centre (address and measurement and town info change) is located less than 50 metres from a public house with a beer garden and under 200 metres from an area starting on St Stephen’s Street designated in City of Edinburgh Council’s Adopted Local Development Plan 2016 as performing a 'town centre' function for Stockbridge.
        5.1.7. On balance, the immediate vicinity surrounding the property is relatively busy, where some level of activity is to be expected. It is considered that for many individuals, the ongoing activity would be regarded as a benefit, comparing favorably with the majority of places elsewhere in Scotland where such activity is absent. The latent activity levels this area enjoys indicates its capacity to assimilate a range of uses within an urban environment that does not appear fragile or sensitive to change.
        The Size of the Property
        5.1.8. (change bedroom and max people and measurement info) The property incorporates a double bedroom and a twin one, capable of hosting a maximum of 4 people and spans approximately 44 sqm. This is smaller than the 52sqm minimum standard for a one-bedroom residential property identified by the City of Edinburgh Council in its January 2020 Design Guidance document, defined to ensure satisfactory amenities.
        5.1.9. (change bedroom and resident count and visitor info) To clarify, a property like this can host either 4 permanent residents (two couples) or 4 visitors (two couples) equally.
        The Pattern of Activity Associated with the Use Including Numbers of Occupants, the Period of Use, Issues of Noise, Disturbance and Parking Demand
        5.1.10. (change guest count info) As noted above, the maximum number of guests that could stay in the property would be 4. The applicant has confirmed that a minimum stay duration of (change amount of nights and month info) 2 nights is implemented throughout most of the year, this total rises to a 4-night minimum stay in August. The property is used as a short-term let an average of 9 nights per calendar month.
        5.1.11. Each guest is screened by the hosting company managing its services. The company's procedures ensure that no one under the age of 25 is allowed to rent the property.
        5.1.12. All guests must agree to 'house rules' for the property at the point of booking. These rules outlaw practices such as smoking or vaping anywhere in the property; holding parties; and keeping pets. The guest book provided to each group of guests explains these rules, providing further detail on matters like refuse disposal and recycling, bag storage and nearby parking, and 'quiet periods' in the property (between 10pm and 7.30am) (hours may change).
        5.1.13. A copy of the property’s guest book as well as a copy of the hosting company’s house rules have been included with this application as supporting documents. Overall, it is believed that there is far greater control of guest behaviour and activity within the property than if it were let out to a permanent resident.
        The Nature and Character of any Services Provided
        5.1.14. Guests arriving by car are directed to suggested local public car parks within the guest book provided with the property. To clarify, the lack of car parking is explicitly stated on the property’s online listing. Anecdotally, the hosting company has confirmed that most guests indeed arrive by train or plane, negating any parking requirement.
        5.1.15. The property has no access to any private or shared outdoor amenity garden areas. (storage rules may change here) It also does not offer any bag storage facilities on-site (although commercial outlets where bag storage is available are suggested in the guest book).
        5.1.16. All cleaning of the property is scheduled after check-out/departures (10.30 am) (times listed here may change) and before check-in/arrivals (4pm). Accordingly, the servicing of the property always takes place in office hours and not during anti- social times.
        """    
},
{
"query":
         """
         'Name': 'Philip John Myerscough', 'Full property address': 'Flat 2F1, 57 Merchiston Crescent, Edinburgh EH10 5AH', 'When did you commence trading as a short term let (approximately)': '01/2019. Ceased 09/2019. Long term let 09/2019 to 06/2020. Recommenced Autumn 2020', 'Number of bedrooms': 'The flat has 3 but we retain 1 and a store cupboard for our own use. So the flat is jet as 2 bedroom; max 4 people', 'Approximate size (sqm)': 'Total approx 135sqm Area let to tenants approx 120sqm', 'Property type (if flat describe floor, shared access, private entrance, etc)': "The flat is on the second floor. The stair serves 6 flats in total. 2 on first floor, 2 on second, 2 on third. The flat is the first on the second floor. The 2 ground floor flats in the building have their own front doors opening to the street. They each have an area of garden sheltering them from the street and the upper flats' entrance.", 'Can you provide a brief history of your ownership of property and description of the property and the area it is located in?': 'The property is a substantial 3 bedroom tenement flat constructed in 1890s in a sought after part of Edinburgh. It has views out over Edinburgh over the stone built villas opposite. Good public transport links. I bought the property in 2009 and substantially reformed it to create a modern, comfortable home for my family. I and my 2/3 children lived exclusively at the property until I retired. In mid 2018 we bought a house in Spain where we now live for most of the year.'
         """,
"answer":
        """
        Assessment
        5.1.1. As Lord Justice Sullivan articulated in his judgement, the Planning Authority is 'entitled' to form an opinion on whether a material change of use has transpired, based on factual matters and degree.
        5.1.2. Moving to the subject property at Flat 2F1, 57 Merchiston Crescent, Edinburgh EH10 5AH (address change here), as previously noted, the 2021 Guidance document cited in section 4 of this Planning Statement provides a comprehensive list of relevant matters that allow for an assessment of the fact and degree of any change from residential use to a short-term let use.
        5.1.3. To assist the Planning Authority in evaluating these matters, the following paragraphs offer some contemplation of the subject property when assessed against these matters.
        The character of the new use and of the wider area
        5.1.4. The short-term let use allows city visitors to reside temporarily in residential properties. Often such stays are marketed as providing opportunities for visitors to 'live like locals'. The essence of such use is on guests acting in a way that they feel like they are permanent residents. This approach ensures that guests who want to embody the idea of living like a local will behave in a manner that is practically indistinguishable from that of a permanent resident.
        5.1.5. In terms of the wider area's character, the property is located in Edinburgh’s sought-after Merchiston area (town info may change). This area is known for its 19th-century architecture and well-connected public transport links. Both permanent residents and visitors should recognize that an urban setting like this can accommodate a variety of urban activities. These might include people and vehicles moving at different times of the day and night, and commercial activities mainly during the day.
        5.1.6. The property at 57 Merchiston Crescent (address and measurement and town info change) is situated in a residential neighbourhood, with a mix of tenement flats and stone-built villas. It is close to several amenities and public transport links.
        5.1.7. Overall, the immediate area around the property is fairly active, with some level of activity reasonably to be expected. The ongoing activity that the area supports would be seen as an advantage rather than an adverse outcome by many people; and compares favorably with perhaps the majority of places elsewhere in Scotland where such activity does not occur. The inherent activity levels in this area also mean that it is capable of assimilating a range of uses in a host urban environment that does not seem fragile or adversely sensitive to change.
        The size of the property
        5.1.8. (change bedroom and max people and measurement info) The property has three bedrooms, with one being retained for personal use. It is advertised as a two-bedroom flat, capable of accommodating a maximum of 4 people. The property extends to approximately 120 sqm, which is considerably larger than the 52sqm minimum standard for a one-bedroom residential property identified by the City of Edinburgh Council in its January 2020 Design Guidance document.
        5.1.9. (change bedroom and resident count and visitor info) To clarify, a property like this can host either 4 permanent residents or 4 visitors.
        The pattern of activity associated with the use including numbers of occupants, the period of use, issues of noise, disturbance and parking demand
        5.1.10. (change guest count info) As noted above, the maximum number of guests that could stay in the property would be 4. The property owner has confirmed that a minimum stay duration of (change amount of nights and month info) 2 nights is in place throughout most of the year, with this total rising to a 4 night minimum stay in August.
        5.1.11. Each guest is vetted by the hosting company managing the property. Under its procedures, the company ensures that no-one under the age of 25 is allowed to rent the property.
        5.1.12. All guests are required to adhere to the 'house rules' for the property at the point of booking. These rules prohibit practices such as: smoking or vaping anywhere in the property; holding parties; and keeping pets. The guest book given to each group of guests outlines these rules and provides further details on matters such as refuse disposal and recycling, bag storage and nearby parking, and 'quiet periods' in the property (between 10pm and 7.30am) (hours may change).
        5.1.13. A copy of the property’s guest book and a copy of the hosting company’s house rules have been appended to this application as supporting documents. Overall, it is considered that there is far greater control of guest behaviour and all activity that can occur in the property than would be the case if it was rented out to a permanent resident.
        The nature and character of any services provided
        5.1.14. Guests arriving by car are directed to suggested local public car parks provided in the guest book. The lack of car parking is clearly stated on the property’s online listing. Anecdotally, the hosting company has confirmed that most guests indeed arrive by train or plane, thus eliminating any need for parking.
        5.1.15. The property does not provide access to any private or shared outdoor amenity garden areas. (storage rules may change here) There are also no bag storage facilities on site (though commercial outlets where bag storage is available are suggested in the guest book).
        5.1.16. All cleaning of the property is scheduled after check-out/departures (10.30 am) (times listed here may change) and before check-in/arrivals (4pm). Accordingly, the servicing of the property always takes place in office hours and not during anti- social times.
        """    
},
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
few_shot_prompt_3 = FewShotPromptTemplate(
    # These are the examples we want to insert into the prompt.
    examples=example_3,
    # This is how we want to format the examples when we insert them into the prompt.
    example_prompt=example_prompt,
    # The prefix is some text that goes before the examples in the prompt.
    # Usually, this consists of intructions.
    prefix = """
        ChatGPT, you are an application writer. Using the new applicant's details and following the structure and style of the original application, I need you to rewrite this application.
        You are an data entry and application writer for the Certificate of Lawful Use for Short-term Let Accommodation: Planning Statement.
        You will be given all the necessary information about the applicant in the input and your task is to follow a specific application format that will be provided and update that application text with the new information given to you as a text.
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