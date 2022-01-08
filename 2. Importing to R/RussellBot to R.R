# Import relevant libraries

library(gsheet)
library(stringr)
library(dplyr)

# Import the sheet we want

russellbot <- gsheet2tbl('docs.google.com/spreadsheets/d/15v7v6THW7qB4MS8cU89dGEzw5CSmPGrMrtkLl_8oJgY/edit#gid=0')

# Silly me from the past labelled the wins as losses as
# characters instead of 1s and 0s so let's replace those now.

russellbot$Result <- str_replace_all(russellbot$Result, 'Win', '1')
russellbot$Result <- str_replace_all(russellbot$Result, 'Loss', '0')

# And transform it into an integer vector as it's currently a character
# vector.

russellbot$Result <- as.integer(russellbot$Result)
russellbot <- as.data.frame(russellbot)

# Creating separate, per map data frames
maps <- unique(russellbot$Map)

for (val in maps) {
  assign(val, filter(russellbot, str_detect(russellbot$Map, val)))
}

