import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# Generate realistic Netflix-like dataset
n_records = 8807

show_ids = [f"s{i}" for i in range(1, n_records + 1)]
types = np.random.choice(['Movie', 'TV Show'], n_records, p=[0.69, 0.31])
titles = [f"Title_{i}" for i in range(1, n_records + 1)]

countries = ['United States', 'India', 'United Kingdom', 'Canada', 'France', 'Japan', 
             'South Korea', 'Spain', 'Mexico', 'Australia', 'Germany', 'Italy', 'Brazil',
             'Turkey', 'Taiwan', 'Thailand', 'Argentina', 'Egypt', 'Nigeria', 'Philippines']
country_list = np.random.choice(countries, n_records, p=[0.35, 0.12, 0.08, 0.05, 0.04, 0.04, 0.03, 0.03, 0.03, 0.03, 0.03, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.01])

start_date = datetime(2008, 1, 1)
end_date = datetime(2021, 9, 30)
date_added = [start_date + timedelta(days=np.random.randint(0, (end_date - start_date).days)) for _ in range(n_records)]
date_added_str = [d.strftime('%B %d, %Y') for d in date_added]

release_years = np.random.randint(1942, 2022, n_records)

ratings = np.random.choice(['TV-MA', 'TV-14', 'TV-PG', 'R', 'PG-13', 'PG', 'TV-Y', 'TV-Y7', 'TV-G', 'G', 'NC-17', 'NR', 'UR'], 
                          n_records, p=[0.28, 0.22, 0.12, 0.10, 0.08, 0.06, 0.04, 0.03, 0.02, 0.02, 0.01, 0.01, 0.01])

durations = []
for t in types:
    if t == 'Movie':
        durations.append(f"{np.random.randint(60, 180)} min")
    else:
        durations.append(f"{np.random.randint(1, 10)} Season{'s' if np.random.randint(1, 10) > 1 else ''}")

genres = ['Dramas', 'Comedies', 'Documentaries', 'Action & Adventure', 'Thrillers', 
          'International Movies', 'Children & Family Movies', 'Romantic Movies', 
          'Horror Movies', 'Sci-Fi & Fantasy', 'Crime TV Shows', 'Reality TV', 
          'Stand-Up Comedy', 'Anime Series', 'Docuseries']

listed_in = []
for _ in range(n_records):
    n_genres = np.random.randint(1, 4)
    selected = np.random.choice(genres, n_genres, replace=False)
    listed_in.append(', '.join(selected))

directors = [f"Director_{np.random.randint(1, 500)}" if np.random.random() > 0.3 else np.nan for _ in range(n_records)]
casts = [', '.join([f"Actor_{np.random.randint(1, 1000)}" for _ in range(np.random.randint(1, 6))]) if np.random.random() > 0.2 else np.nan for _ in range(n_records)]
descriptions = [f"Description for {title}" for title in titles]

df = pd.DataFrame({
    'show_id': show_ids,
    'type': types,
    'title': titles,
    'director': directors,
    'cast': casts,
    'country': country_list,
    'date_added': date_added_str,
    'release_year': release_years,
    'rating': ratings,
    'duration': durations,
    'listed_in': listed_in,
    'description': descriptions
})

df.to_csv('data/netflix_titles.csv', index=False)
print(f"Dataset created: {len(df)} records")
print(df.head())
