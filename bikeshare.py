import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city != 'chicago' and city != 'new york city' and city != 'washington':
        city = input('Which city would you like to choose? Enter Chicago, New York City or Washington: ')
        city = city.lower()

    # get user input for month (all, january, february, ... , june)
    month = ''
    while month != 'january' and month != 'february' and month != 'march' and month != 'april' and month != 'may' and month != 'june' and month != 'all':
        month = input('Which month would you like to filter by? Enter January, February, March, April, May, June, or all: ')
        month = month.lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day != 'monday' and day != 'tuesday' and day != 'wednesday' and day != 'thursday' and day != 'friday' and day != 'saturday' and day != 'sunday' and day != 'all':
        day = input('Which day would you like to filter by? Choose from Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all: ')
        day = day.lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    # correct indices
    n = df.shape[0]
    index_new = list(range(n))
    df.index = index_new
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = months[popular_month - 1].capitalize()
    
    print('Most Popular Start Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Start Day:', popular_day)

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'] + ' and ' + df['End Station']
    popular_start_end = df['Start End'].mode()[0]
    print('Most Popular Start and End Station:', popular_start_end)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total travel time is {} seconds'.format(total_travel))
    
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean travel time is {} seconds'.format(mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User type count:', user_types)
    
    # TO DO: Display counts of gender
    gender_count = df['Gender'].value_counts()
    print('Gender count:', gender_count)
    
    # TO DO: Display earliest, most recent, and most common year of birth
    birth_earliest = df['Birth Year'].min()
    birth_recent = df['Birth Year'].max()
    birth_common = df['Birth Year'].mode()
    print('Earliest year of birth:', birth_earliest)
    print('Most recent year of birth:', birth_recent)
    print('Most common year of birth:', birth_common)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        # load data
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        # print 5 rows at a time
        df2 = df
        raw_data = input('\nWould you like to browse through the data? Enter yes or no.\n')
        if raw_data.lower() == 'yes':
            print(df2.head())
        a,b,c,d,e = 0,1,2,3,4
        while raw_data.lower() == 'yes':
            raw_data = input('\nWould you like to browse further? Enter yes or no.\n')
            if raw_data.lower() == 'yes':
                df2.drop([a,b,c,d,e], axis = 0, inplace = True)
                print(df2.head())
                a += 5
                b += 5
                c += 5
                d += 5
                e += 5

            else:
                break

        continue1 = input('\nWould you like to display statistics on the most frequent times of travel? Enter yes to continue or no to stop.\n')
        if continue1.lower() != 'yes':
            break        

        time_stats(df)
        
        continue2 = input('\nWould you like to display statistics on the most popular stations and trip? Enter yes to continue or no to stop.\n')
        if continue2.lower() != 'yes':
            break
            
        station_stats(df)
        
        continue3 = input('\nWould you like to display statistics on the total and average trip duration? Enter yes to continue or no to stop.\n')
        if continue3.lower() != 'yes':
            break
            
        trip_duration_stats(df)
        
        continue4 = input('\nWould you like to display statistics on bikeshare users? Enter yes to continue or no to stop.\n')
        if continue4.lower() != 'yes':
            break
            
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
