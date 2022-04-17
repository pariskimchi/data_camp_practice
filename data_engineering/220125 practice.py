
# complete the transformation function 

def transform_avg_rating(rating_data):
    # Group by course_id and extrace avg rating per course 
    avg_rating = rating_data.groupBy("course_id").rating.mean()

    # return sorted avg ratings per course 
    sort_rating = avg_rating.sort_values(ascending=False).reset_index()
    return sort_rating

# Extract the rating data into a DataFrame 
rating_data = extract_rating_data(db_engines)

# use Transform_avg_rating on the extracted data and print results 
avg_rating_data = transform_avg_rating(rating_data)
print(avg_rating_data)