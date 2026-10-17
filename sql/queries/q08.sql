-- Q8: Cricket series that started in the year 2024
SELECT series_name, host_country, match_type, start_date, total_matches FROM series WHERE strftime('%Y', start_date) = '2024';