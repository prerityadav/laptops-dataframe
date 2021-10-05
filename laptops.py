import pandas as pd
 
laptop_data = pd.DataFrame(
    {
        "laptop_brands": ["HP","DELL","APPLE", "ASUS"],
        "features": ["9 gb RAM"," 7 gb RAM","12 gb RAM", "4 gb RAM"],
        "prices": ["$21,000", "$19,000", "$35,000", "$15,000"],
    }
)


print(laptop_data)
