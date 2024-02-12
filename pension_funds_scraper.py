import requests
from bs4 import BeautifulSoup
import csv

# Replace with your actual API key and Custom Search Engine ID
api_key = ''
search_engine_id = ''  # Replace with your actual Search Engine ID

# Function to perform Google search and check for "emerging manager"
def check_emerging_manager_program(fund_name):
    search_query = f"{fund_name} emerging manager"
    url = f"https://www.googleapis.com/customsearch/v1?q={search_query}&key={api_key}&cx={search_engine_id}"

    # Make the request to Google Custom Search API
    response = requests.get(url)
    data = response.json()

    # Check if there are any items in the search results
    if 'items' in data:
        return "Has Emerging Manager"
    else:
        return "Does Not Have Emerging Manager"

# List of pension funds
pension_funds = [
    "Federal Retirement Thrift",
    "California Public Employees",
    "California State Teachers",
    "New York State Common",
    "New York City Retirement",
    "Florida State Board",
    "Texas Teachers",
    "Washington State Board",
    "Wisconsin Investment Board",
    "Boeing",
    "New York State Teachers",
    "North Carolina",
    "California University",
    "Ohio Public Employees",
    "AT&T",
    "IBM",
    "Virginia Retirement",
    "Raytheon Technologies",
    "Michigan Retirement",
    "New Jersey",
    "Minnesota State Board",
    "Kaiser",
    "Georgia Teachers",
    "Oregon Public Employees",
    "Massachusetts PRIM",
    "General Motors",
    "Ohio State Teachers",
    "General Electric",
    "United Parcel Service",
    "United Nations Joint Staff",
    "Lockheed Martin",
    "Tennessee Consolidated",
    "Bank of America",
    "Ford Motor",
    "Los Angeles County Empl.",
    "Northrop Grumman",
    "Pennsylvania School Empl.",
    "Colorado Employees",
    "Maryland State Retirement",
    "Wells Fargo",
    "Verizon",
    "Illinois Teachers",
    "J.P. Morgan Chase",
    "FedEx",
    "Nevada Public Employees",
    "Missouri Schools & Educ.",
    "Illinois Municipal",
    "Teamsters, Western Conf.",
    "Utah State Retirement",
    "Johnson & Johnson",
    "State Farm",
    "Arizona State Retirement",
    "South Carolina Public Empl.",
    "Alabama Retirement",
    "Delta Air Lines",
    "Indiana Public Retirement",
    "Nokia USA",
    "Iowa Public Employees",
    "Pennsylvania Employees",
    "Alaska Retirement",
    "Connecticut Retirement",
    "Texas County & District",
    "Microsoft",
    "San Francisco City & County",
    "Texas Employees",
    "American Airlines",
    "Federal Reserve Employees",
    "Pfizer",
    "Honeywell",
    "Mississippi Employees",
    "Walmart",
    "Exxon Mobil",
    "Texas Municipal Retirement",
    "3M",
    "General Dynamics",
    "New York State Def. Comp.",
    "CVS Health",
    "Walt Disney",
    "Caterpillar",
    "Citigroup",
    "Exelon",
    "United Airlines Holdings",
    "Shell Oil",
    "Los Angeles Fire & Police",
    "PepsiCo",
    "Chevron",
    "National Electric",
    "World Bank",
    "Illinois State Board",
    "PG&E",
    "FCA US",
    "Louisiana Teachers",
    "Intel",
    "Costco Wholesale",
    "Dow",
    "New York City Def. Comp.",
    "National Railroad",
    "Deloitte",
    "Illinois State Universities",
    "Ascension",
    "Ernst & Young",
    "Procter & Gamble",
    "Kansas Public Employees",
    "CommonSpirit Health",
    "Merck",
    "FMR",
    "Truist Financial",
    "Abbott Laboratories",
    "National Rural Electric",
    "Deere",
    "Alphabet",
    "Kentucky Teachers",
    "Prudential Financial",
    "Southern Co.",
    "Corteva",
    "SUNY",
    "L3Harris Technologies",
    "Operating Eng. International",
    "Duke Energy",
    "Consolidated Edison",
    "Idaho Public Employees",
    "Wespath (UMC)",
    "Los Angeles City Employees",
    "Georgia Employees",
    "Oracle",
    "Mass General Brigham",
    "Morgan Stanley",
    "Nebraska Investment Council",
    "Oklahoma Teachers",
    "HCA Holdings",
    "Hawaii Employees",
    "Orange County",
    "Eli Lilly",
    "Arkansas Teachers",
    "Liberty Mutual",
    "New York City Teachers",
    "West Virginia Investment",
    "California Savings Plus",
    "Los Angeles Co. Deferred",
    "Ohio Deferred Comp.",
    "Providence Health",
    "Koch Industries",
    "Los Angeles Water & Power",
    "Episcopal Church",
    "UnitedHealth",
    "Mayo Clinic",
    "International Paper",
    "PricewaterhouseCoopers",
    "New Mexico Public Empl.",
    "MetLife",
    "Ohio Police & Fire",
    "New York City MTA",
    "Maine Public Employees",
    "Lumen Technologies",
    "Ohio School Employees",
    "Target",
    "Cisco Systems",
    "Toyota USA",
    "AbbVie",
    "U.S. Bancorp",
    "Dominion Energy",
    "National Grid USA",
    "1199SEIU National",
    "USAA",
    "Accenture",
    "Cigna",
    "Medtronic",
    "BAE (NA)",
    "HP",
    "San Diego County",
    "Roche USA",
    "Comcast Holdings",
    "Bayer",
    "Publix Super Markets",
    "Arizona Public Safety",
    "Southwest Airlines",
    "New Mexico Educational",
    "National Elevator Industry",
    "Kentucky Public Pensions",
    "Bank of New York Mellon",
    "Kroger",
    "Cox Enterprises",
    "IAM National",
    "BP America",
    "South Dakota",
    "Sammons Enterprises",
    "Blue Cross & Blue Shield",
    "Michigan Municipal",
    "PNC",
    "Dell Technologies",
    "Delaware Public Employees",
    "Montana Board of Invest.",
    "Nationwide",
    "University of Pennsylvania",
    "Apple",
    "Sacramento County",
    "Oklahoma Public Employees",
    "Electrical Ind., Joint Board",
    "New York Life",
    "KPMG",
    "Amazon.com",
    "Walgreens Boots Alliance",
    "Travelers",
    "Allstate",
    "Huntington Ingalls",
    "Sutter Health",
    "San Bernardino County",
    "Louisiana State Employees",
    "Textron",
    "FirstEnergy",
    "Deseret Mutual Benefit",
    "Altria",
    "Cook County Employees",
    "Tennessee Valley Authority",
    "IMF",
    "Schlumberger",
    "Coca-Cola",
    "Presbyterian Church",
    "Anthem",
    "Chicago Teachers",
    "Marsh McLennan",
    "NTESS",
    "NextEra Energy",
    "General Mills",
    "MIT",
    "Massachusetts Def. Comp.",
    "GlaxoSmithKline USA",
    "Cargill",
    "NYU",
    "Missouri State Employees",
    "Nestle USA",
    "Northwell Health",
    "Pentegra",
    "Rhode Island Employees",
    "American Int'l Group",
    "Novartis US",
    "Longshoremen ILWU-PMA",
    "Cleveland-Cliffs",
    "Sherwin-Williams",
    "Public Service Enterprise",
    "American Electric",
    "Charter Communications",
    "Goodyear Tire & Rubber",
    "Entergy",
    "Home Depot",
    "Arkansas Employees",
    "Wyoming Retirement",
    "Alameda County",
    "New Hampshire Retirement",
    "Parker-Hannifin",
    "Eaton",
    "Contra Costa County",
    "Cleveland Clinic",
    "Duke University",
    "Mars",
    "Hartford Financial",
    "Stanford University",
    "American Honda Motor",
    "Motorola Solutions",
    "UPMC",
    "D.C. Retirement Board",
    "Marriott International",
    "Goldman Sachs",
    "BASF USA",
    "Marathon Petroleum",
    "Motion Picture Industry",
    "San Diego City",
    "UNC-Chapel Hill",
    "Boilermaker-Blacksmith",
    "Northwestern Mutual",
    "Eversource Energy",
    "Union Pacific",
    "Johnson Controls",
    "WestRock",
    "Missouri Local Gov't",
    "T-Mobile",
    "Texas Instruments",
    "Albertsons",
    "HSBC USA",
    "Leidos",
    "Siemens USA",
    "Edward Jones",
    "DTE Energy",
    "Reynolds American",
    "Southern California Edison",
    "Hewlett Packard Enterprise",
    "Tenet Healthcare",
    "Sysco",
    "UBS Financial Services",
    "UBS Investment Bank",
    "ViacomCBS",
    "Kraft Heinz",
    "Southern Baptist Convention",
    "Harvard University",
    "Burlington N. Santa Fe",
    "McKinsey",
    "ConocoPhillips",
    "Phillips 66",
    "Bristol-Myers Squibb",
    "Emerson Electric",
    "Utah Higher Education",
    "Fairfax County Retirement",
    "Sanofi-Aventis",
    "Trinity Health",
    "Danaher",
    "YMCA",
    "Ameren",
    "United States Steel",
    "Vanguard Group",
    "Sempra Energy",
    "Capital One Financial",
    "Aon",
    "Los Angeles City Def. Comp.",
    "Teamsters, Central States",
    "Carpenters, New York City",
    "TIAA",
    "Cummins",
    "American Express",
    "University of S. Calif.",
    "MUFG Americas",
    "Southwest Airlines Pilots",
    "Carpenters, N. Calif.",
    "Thermo Fisher Scientific",
    "NFL Player Benefits",
    "AstraZeneca US",
    "Carpenters, North Atlantic",
    "Farmers Group",
    "Chubb",
    "Columbia University",
    "Corning",
    "Bridgestone Americas",
    "Xcel Energy",
    "Evangelical Lutheran Church",
    "Willis Towers Watson",
    "Lowes",
    "Yale University",
    "Cornell University",
    "UMWA Health & Retirement",
    "Intermountain Healthcare",
    "Howmet Aerospace",
    "Macy's",
    "Mount Sinai",
    "ADP",
    "UFCW Industry, Ill.",
    "ABA Retirement",
    "University of Chicago",
    "MassMutual",
    "Ventura County",
    "Plumbers & Pipefitters Nat'l",
    "Pactiv Evergreen",
    "Michigan State University",
    "WEC Energy Group",
    "TriNet Group",
    "MITRE",
    "Sheet Metal National",
    "United Natural Foods",
    "North Dakota State",
    "Progressive",
    "Colorado Fire & Police",
    "Michelin",
    "AECOM",
    "Qualcomm",
    "Amgen",
    "Booz Allen Hamilton",
    "Becton, Dickinson",
    "SAP America",
    "Rockwell Automation",
    "Xerox",
    "John Hancock",
    "Credit Suisse (USA)",
    "Ingersoll-Rand",
    "Equitable Holdings",
    "Humana",
    "Broadcom",
    "Siemens Healthineers USA",
    "Houston Police Officers",
    "Philadelphia Public Empl.",
    "Schneider Electric USA",
    "National Sprinkler Local 669",
    "Chicago City Def. Comp.",
    "Philips",
    "Highmark",
    "Thomson Reuters",
    "Eastman Kodak",
    "Ecolab",
    "Savannah River",
    "State Street",
    "Alaska Air",
    "Vermont Pension",
    "Memorial Sloan-Kettering",
    "Charles Schwab",
    "Whirlpool",
    "Kimberly-Clark",
    "PPL",
    "Montgomery County",
    "Steelworkers Pension",
    "Boston Retirement",
    "J.C. Penney",
    "Battelle",
    "Insperity",
    "University of Rochester",
    "California Institute of Tech.",
    "Washington University",
    "Air Products & Chemicals",
    "UFCW Joint Trust, S. Calif.",
    "Capital Group",
    "CMS/Consumers Energy",
    "Carpenters, Chicago",
    "Carpenters, Southwest",
    "Valero Energy",
    "Fresno County",
    "Jacobs Engineering",
    "Service Empl. 32B & 32J",
    "Bechtel Global",
    "Nissan USA",
    "Transamerica",
    "Ericsson",
    "Army & Air Force Exchange",
    "PPG Industries",
    "Pinnacle West",
    "CSX",
    "Principal Financial",
    "Saint-Gobain",
    "Conagra Brands",
    "Nucor",
    "Deutsche Bank USA",
    "Milwaukee City",
    "Manufacturers & Traders",
    "Robert Bosch",
    "San Mateo County",
    "Frontier Communications",
    "Illinois Tool Works",
    "Avangrid",
    "Nike",
    "Anheuser-Busch InBev",
    "GEICO",
    "Sentara Healthcare",
    "Operating Eng. Local 3",
    "Unisys",
    "Fiserv",
    "Facebook",
    "Adventist Healthcare",
    "Eastman Chemical",
    "Colgate-Palmolive",
    "XPO Logistics",
    "NTCA",
    "Saudi Arabian Oil",
    "Alcoa",
    "UFCW, Atlanta",
    "BJC HealthCare",
    "S&P Global",
    "ECA & Local 134 IBEW",
    "Stryker",
    "University of Kentucky",
    "Inter-Amer. Dev. Bank",
    "Quest Diagnostics",
    "Kellogg",
    "Baxter International",
    "Kern County Employees",
    "Norfolk Southern",
    "Health Care Service",
    "Regions Financial",
    "New York State Nurses",
    "Comerica",
    "Maryland Supplemental",
    "Hearst",
    "Ball",
    "Boston Scientific",
    "Houston Firefighters",
    "Florida Deferred Comp.",
    "Linde",
    "Takeda Pharmaceuticals",
    "RELX",
    "Operating Eng. Midwest",
    "CenterPoint Energy",
    "Lutherans-Mo. Synod",
    "Bechtel Marine Propulsion",
    "Zurich American",
    "Sony America",
    "Painters & Allied Trades",
    "Weyerhaeuser",
    "Science Applications Int'l",
    "Kinder Morgan",
    "Community Health",
    "Carpenters, New Jersey",
    "TD Bank",
    "TJX",
    "CNA Financial",
    "Kansas Regents",
    "Burns & McDonnell",
    "KeyCorp",
    "FM Global",
    "Major League Baseball",
    "Voya Financial",
    "PACCAR",
    "Stanford Hospital",
    "Applied Materials",
    "Parsons",
    "Northern Trust",
    "San Jose Federated City",
    "San Jose Police & Fire",
    "University of Nebraska",
    "Boehringer Ingelheim",
    "Northwestern University",
    "Maryland Optional",
    "Enterprise Rent-A-Car",
    "Salesforce.com",
    "Guardian Life",
    "Molson Coors Brewing",
    "Nashville & Davidson County",
    "Louisiana Sheriffs",
    "FIS",
    "Carpenters, Ohio",
    "Atlanta City",
    "Halliburton",
    "Emory University",
    "Meijer",
    "SAG-Producers",
    "RWJBarnabas Health",
    "Archer Daniels Midland",
    "Pipefitters Local 597",
    "Louisiana Parochial Empl.",
    "Cardinal Health",
    "CRH Americas",
    "Genuine Parts",
    "Amsted Industries",
    "Ahold Delhaize USA",
    "Laborers, Chicago & Vicinity",
    "Citizens Financial",
    "Banner Health",
    "Allina Health",
    "H-E-B",
    "Auto Club of S. Calif.",
    "Salt River Valley",
    "McDonald's",
    "Bloomberg",
    "Tyco Electronics",
    "American Family",
    "Carpenters, Empire State",
    "UFCW, N. Calif.",
    "Fresno City Retirement",
    "American Nat'l Red Cross",
    "Kentucky Deferred Comp.",
    "Bakery & Confectionery",
    "Iron Workers, Calif.",
    "JetBlue Airways",
    "Unum Group",
    "Oncor Electric Delivery",
    "Houston Municipal",
    "San Antonio Fire & Police",
    "Santa Barbara County",
    "Hallmark Cards",
    "Seattle City Employees",
    "Dun & Bradstreet",
    "Omnicom Group",
    "Dallas City Employees",
    "San Joaquin County",
    "Manhattan & Bronx Surface",
    "University of Wisconsin",
    "Fifth Third",
    "Olin",
    "United Church of Christ",
    "Santa Clara County Def.",
    "Navistar",
    "Graham Holdings",
    "Montefiore Medical Center",
    "Operating Eng. Local 18",
    "Johns Hopkins",
    "Teamsters Local 710",
    "Fluor",
    "Rite Aid",
    "NiSource",
    "Chicago Municipal Empl.",
    "Precision Castparts",
    "Estee Lauder",
    "Laborers International",
    "Ryder System",
    "Savings Banks Employees",
    "Fannie Mae",
    "Tyson Foods",
    "LyondellBasell",
    "LSC Communications",
    "University of Miami",
    "SAS Institute",
    "Waste Management",
    "NXP Semiconductors",
    "NCR",
    "Sentry Insurance",
    "Interpublic Group",
    "Vanderbilt U. Medical Center",
    "Smithfield Foods",
    "Unilever USA",
    "Christian Church (Disciples)",
    "BlackRock",
    "Baltimore County",
    "Hanford Site",
    "Nexstar Media Group",
    "RBC Wealth Mgmt.",
    "Pitney Bowes",
    "IBEW International",
    "Carpenters, St. Louis",
    "Oklahoma Firefighters",
    "W.W. Grainger",
    "Barclays Bank",
    "Harley-Davidson",
    "Gannett",
    "Ricoh USA",
    "Visa",
    "Phoenix City Employees",
    "National Railroad Passenger",
    "Laborers Local 731",
    "Baltimore Fire & Police",
    "Service Empl. Int'l",
    "Aerospace",
    "Hormel Foods",
    "US Foods",
    "Cerner",
    "Sonoma County",
    "Mastercard",
    "Hess",
    "UnityPoint Health",
    "Allegheny Technologies",
    "Pennsylvania Municipal",
    "Cincinnati Children's",
    "Tenneco",
    "Evergy",
    "Blue Cross/Shield of Mich.",
    "Austin Employees",
    "Princeton University",
    "Marin County Employees",
    "Thrivent Fin'l for Lutherans",
    "Iowa Fire & Police",
    "Georgetown University",
    "Hawaiian Electric Industries",
    "Land O'Lakes",
    "Williams",
    "Los Angeles County MTA",
    "Fairfax County Education",
    "Starbucks",
    "Carpenters, Philadelphia",
    "Sidley Austin",
    "New York Times",
    "Hawaii Deferred Comp.",
    "Micron Technology",
    "Henkel",
    "Oklahoma Police",
    "Newell Brands",
    "Memphis City",
    "Advance Publications",
    "Adobe Systems",
    "Hershey",
    "Jacksonville Retirement",
    "Westinghouse Electric",
    "AFTRA",
    "Arlington County",
    "CBRE",
    "NYC Hotel Trades",
    "Assurant",
    "Georgia Municipal",
    "Retail Clerks, Wash.",
    "Intercontinental Exchange",
    "Ark. Local Police & Fire",
    "DXC Technology",
    "Cintas",
    "IBEW 11, 440, 441, 477",
    "Discover",
    "University of Alabama",
    "Operating Eng. Local 12",
    "Building Trades United",
    "Andersen",
    "Freddie Mac",
    "MPERS",
    "SS&C Technologies",
    "Sonoco Products",
    "Universal Health Services",
    "Operating Eng. 302 & 612",
    "Verisk Analytics",
    "Jones Lang LaSalle",
    "Solvay USA",
    "East Bay Municipal Utility",
    "Avaya",
    "PacifiCorp",
    "L'Oreal USA",
    "Quad/Graphics",
    "Pipe Trades, Twin Cities",
    "Triumph Group",
    "United Steelworkers Int'l",
    "Christiana Care Health",
    "Ameriprise Financial",
    "Jones Day",
    "George Washington U.",
    "VF Corp.",
    "Laborers, S. Calif.",
    "Clorox",
    "Wellington Mgmt.",
    "Chicago Policemen",
    "General Re",
    "Equity League",
    "Fox",
    "Analog Devices",
    "Kohler",
    "Owens-Illinois",
    "Office Depot",
    "Laborers, Minnesota",
    "UMass Memorial Health",
    "Fort Worth Employees",
    "CITGO Petroleum",
    "Detroit Police & Fire",
    "IBEW Local 103",
    "Huntington Bancshares",
    "Rolls-Royce (NA)",
    "Magna Int'l of America",
    "BMW USA",
    "Wake Forest Baptist Medical",
    "Owens Corning",
    "Hy-Vee",
    "Tampa Fire & Police",
    "Phoenix City Def. Comp.",
    "Depository Trust & Clearing",
    "Stanislaus County",
    "Louisiana Muni. Police",
    "Latham & Watkins",
    "Tallahassee City",
    "Best Buy",
    "CHS",
    "Chicago Transit Authority",
    "Lubrizol",
    "Anne Arundel County",
    "Laborers, Ohio",
    "Fidelity National",
    "Denver Employees",
    "McMaster-Carr Supply",
    "Pearson",
    "Syngenta",
    "University of Oregon",
    "Trader Joe's",
    "Allianz of America",
    "Seafarers",
    "Carnegie Mellon University",
    "Christian Brothers",
    "Cincinnati City",
    "Valvoline",
    "Stanley Black & Decker",
    "Operating Eng. Local 825",
    "Lam Research",
    "Iowa Administrative Services",
    "Keysight Technologies",
    "Jacksonville Police & Fire",
    "Syracuse University",
    "Swagelok",
    "Mutual of Omaha",
    "Intuit",
    "Teamsters, Central Pa.",
    "Windstream",
    "Hilton Hotels",
    "Fulton County",
    "Vanderbilt University",
    "Teamsters Trucking, N.E.",
    "Western Digital",
    "USG",
    "Alaska Electrical",
    "SEPTA",
    "Industrial Workers Timber",
    "Seagate Technology",
    "FMC",
    "Lehigh Hanson",
    "Carpenters, Western Wash.",
    "McDermott",
    "Sodexo",
    "Teamsters, Philadelphia",
    "Volvo Group",
    "Transocean",
    "Ametek",
    "Suffolk County Def. Comp.",
    "Teva USA",
    "Old Republican Int'l",
    "Gap",
    "Dover",
    "Blue Cross/Shield of Mass.",
    "UFCW International, D.C.",
    "Nielsen",
    "Snap-on",
    "Bimbo Bakeries USA",
    "University of Notre Dame",
    "ARAMARK",
    "TOTAL",
    "Vulcan Materials",
    "Black & Veatch",
    "Dartmouth College",
    "Graybar Electric",
    "Carpenters, Illinois",
    "MidAmerican Energy",
    "National Oilwell Varco",
    "GROWMARK",
    "University of Louisville",
    "Dana",
    "Roofers United",
    "Aerojet Rocketdyne",
    "Colorado County",
    "Levi Strauss",
    "Woodward",
    "Louisiana Firefighters",
    "Enbridge",
    "Penske Truck Leasing",
    "Cook County Def. Comp.",
    "San Diego Co. Def. Comp.",
    "Yum Brands",
    "TECO Energy",
    "National Football League",
    "Brown University",
    "LafargeHolcim US",
    "Louisiana Deferred Comp.",
    "TRW Automotive Holdings",
    "NV Energy",
    "Cultural Institutions",
    "First American",
    "Case New Holland",
    "Carpenters, N. Central Sts.",
    "S. C. Johnson & Son",
    "First Data",
    "TechnipFMC USA",
    "Energy Transfer",
    "Bemis",
    "Food & Comm. Local 27",
    "Dairy Farmers",
    "Aptiv",
    "Hubbell",
    "Puget Sound Energy",
    "Detroit General Retirement",
    "Louisiana Schools",
    "IBEW Local 68, District 8",
    "New Jersey Transit",
    "Northeastern University",
    "BorgWarner",
    "Tacoma Employees",
    "Baltimore City",
    "MGM Resorts Int'l",
    "Verso",
    "Wolters Kluwer",
    "Panasonic USA",
    "Reform Pension",
    "Tulare County",
    "Underwriters Laboratories",
    "Carpenters, Twin Cities",
    "YRC Worldwide",
    "Twin City Hospital, Nurses",
    "Agilent Technologies",
    "Kohl's",
    "Skadden, Arps, Slate",
    "American Fed. of Musicians",
    "Chicago Public Schools",
    "Evonik (NA)",
    "Nassau County Def. Comp.",
    "Stationary Engineers 39",
    "Middlesex County",
    "San Luis Obispo County",
    "Bank of the West",
    "Republic Services",
    "Rio Tinto America",
    "L Brands",
    "Portland General Electric",
    "Baptist Health South Florida",
    "Crane",
    "Fortune Brands Hm. & Sec.",
    "Telephone & Data Systems",
    "IBEW Local 26",
    "Essentia Health",
    "Keurig Dr Pepper",
    "Dallas Police & Fire",
    "University of Maine",
    "AFSCME",
    "Bricklayers International",
    "CPS Energy",
    "Bertelsmann",
    "Cognizant",
    "Equifax",
    "El Paso Fire & Police",
    "Patterson",
    "Iron Workers 40, 361, 417",
    "Navy Exchange",
    "Philadelphia City Def. Comp.",
    "Timken",
    "California State University",
    "Operating Eng. Local 15",
    "First Horizon",
    "Franklin Resources",
    "Boy Scouts of America",
    "Milwaukee County",
    "Bombardier Motor",
    "MBTA Retirement",
    "AAA N. Calif., Nev. & Utah",
    "Carpenter Technology",
    "Deluxe",
    "Graphic Packaging",
    "SKF USA",
    "Teamsters, N.Y. State Conf.",
    "Alliant Energy",
    "Lexmark International",
    "Arizona Deferred Comp.",
    "Talen Energy",
    "Hanesbrands",
    "ONE Gas",
    "DLA Piper",
    "Saint Louis University",
    "Carpenters, Greater Pa.",
    "W.R. Grace",
    "Brunswick",
    "Longshoremen NYSA ILA",
    "Teamsters Local 705",
    "Old Dominion Freight Line",
    "Howard Hughes Medical",
    "Fujitsu America",
    "Cambridge Retirement",
    "MARTA",
    "Sealed Air",
    "Independence Blue Cross",
    "Huntsman",
    "W.R. Berkley",
    "Hanover Insurance",
    "Southern Electrical Ret.",
    "BHP",
    "Steelcase",
    "DeKalb County Employees",
    "IBEW Local 1",
    "Advanced Micro Devices",
    "Caesars Entertainment",
    "Flowserve",
    "Weil, Gotshal & Manges",
    "National Fuel Gas",
    "Meritor",
    "Smiths Group",
    "Arkansas State Highway",
    "Memphis Light Gas & Water",
    "Western & Southern Life",
    "CFI",
    "Crown Holdings",
    "Operating Eng. 94, 94a, 94b",
    "Peabody",
    "MDU Resources",
    "NVR",
    "Wayne County",
    "SRI International",
    "Bausch Health",
    "Albemarle",
    "Plymouth County Retirement",
    "Teamsters Local 639",
    "Brown-Forman",
    "CIT Group",
    "Marine Engineers",
    "Laborers National",
    "TimkenSteel",
    "Operating Eng. Local 324",
    "Orlando City",
    "Auto Workers National",
    "Alticor",
    "Electrolux",
    "Wichita Retirement",
    "B&W Technical Y-12",
    "Staples",
    "Washington Gas Light",
    "Michigan Catholic Conf.",
    "Sappi",
    "Devon Energy",
    "Laborers, Indiana",
    "Chicago MWRD Retirement",
    "ALSTOM",
    "Sabre Holdings",
    "BMO Financial",
    "Hartford HealthCare",
    "Lincoln National",
    "Campbell Soup",
    "Mondelez International",
    "Producer-Writers Guild",
    "Directors Guild-Producer",
    "Publicis USA",
    "WMATA Retirement",
    "University of Mo. Curators",
    "MedStar Health",
    "Freeport-McMoRan",
    "Daimler Trucks",
    "T . Rowe Price",
    "Fresenius Medical Care",
    "Wawa",
    "Amica Mutual Insurance",
    "Nordstrom",
    "ABB",
    "KBR",
    "Beaumont Hospitals",
    "Laborers, Massachusetts",
    "Montgomery Public Schools",
    "HDR",
    "Winco Foods",
    "Boston University",
    "McKesson",
    "Nevada Higher Education",
    "Laboratory Corp. of America",
    "Baker Hughes",
    "Idaho National Laboratory",
    "Occidental Petroleum",
    "Celanese Americas"
    # Add more funds here...
]

# Open a CSV file to write the results
with open('pension_funds_results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Pension Fund', 'Emerging Manager Program'])

    # Iterate through each pension fund
    for fund in pension_funds:
        result = check_emerging_manager_program(fund)
        writer.writerow([fund, result])

print("Scraping complete. Results saved in pension_funds_results.csv.")
