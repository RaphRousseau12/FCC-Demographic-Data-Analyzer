import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    df_race = df['race'].value_counts()
    race_count = df_race

    # What is the average age of men?
    df_male = df[df['sex'] == 'Male']
    df_male_average_age = round(df_male['age'].mean(), 1)
    average_age_men = df_male_average_age


    # What is the percentage of people who have a Bachelor's degree?
    df_bachelors = df[df['education'] == 'Bachelors']
    bachelors_count = len(df_bachelors)
    total_count = len(df)

    percentage_bachelors = round(bachelors_count / total_count * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_count = len(higher_education)
    higher_education_50k = higher_education[higher_education['salary'] == '>50K']
    higher_education_50k_count = len(higher_education_50k)
    
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_count = len(lower_education)
    lower_education_50k = lower_education[lower_education['salary'] == '>50K']
    lower_education_50k_count =  len(lower_education_50k)


    # percentage with salary >50K
    higher_education_rich = round(higher_education_50k_count / higher_education_count * 100, 1)
    lower_education_rich = round(lower_education_50k_count / lower_education_count * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    df_work_hours = df['hours-per-week']
    min_work_hours = df_work_hours.min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df_min = df[df['hours-per-week'] == min_work_hours]
    df_min_count = len(df_min)
    df_50k_salary_min_hours = df_min[df_min['salary'] == '>50K']
    df_50k_salary_min_hours_count = len(df_50k_salary_min_hours)

    rich_percentage =  df_50k_salary_min_hours_count / df_min_count * 100

    # What country has the highest percentage of people that earn >50K?
    df_50k_salary = df[df['salary'] == '>50K']
    df_50k_country_salary_counts = df_50k_salary['native-country'].value_counts()
    df_counts = df['native-country'].value_counts(ascending=True)
    df_percentage_country = round(df_50k_country_salary_counts / df_counts * 100, 1)
    
    highest_earning_country = df_percentage_country.idxmax()
    highest_earning_country_percentage = df_percentage_country.max()

    # Identify the most popular occupation for those who earn >50K in India.
    df_IN = df[df['native-country'] == 'India']
    df_IN_50k = df_IN[df_IN['salary'] == '>50K']
    top_IN_occupation = df_IN_50k['occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
