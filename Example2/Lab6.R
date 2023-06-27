install.packages("jsonlite", repos="https://cran.rstudio.com/")
# Package names
packages <- c("tidyverse", "jsonlite", "tcltk", "dplyr", "ggpubr", "psych", "mnormt", "lubridate")

# Install packages not yet installed
installed_packages <- packages %in% rownames(installed.packages())
if (any(installed_packages == FALSE)) {
  install.packages(packages[!installed_packages])
}

# Packages loading
invisible(lapply(packages, library, character.only = TRUE))

#Checking how the data is organized
info <- read.csv('Info_Data.csv')
head(info)

#Creating the dataset to be analyzed
interpol_data <- read.csv('Interpolated_Data.csv')
lakeGeorge <- filter(interpol_data, lake_id == 131)

#Check max depth
summary(lakeGeorge$depth) #goes down 33m max



#Make the date format useable
lakeGeorge$date <- as.Date(lakeGeorge$date)
head(lakeGeorge) #1980-06-03 chosen as date



#surface temp mean calculation for surface temp is depth <= 10m
lakeGeorgeSurface <- filter(lakeGeorge, depth <= 10)

lakeGeorgeSurfMean <- lakeGeorgeSurface %>% group_by(date) %>% summarise(surfTemp = mean(temp), surf_do_con = mean(do_con))

head(lakeGeorgeSurfMean)



#Get only Summer months
lakeGeorgeSurfMean$month <- month(lakeGeorgeSurfMean$date)

lakeGeorgeSurfMean_summary <- filter(lakeGeorgeSurfMean, month == 7 | month ==8)

lakeGeorgeSurfMean_summary$year <- year(lakeGeorgeSurfMean_summary$date)

head(lakeGeorgeSurfMean_summary)



#assign how many measurements for each year
lakeGeorgeSurfMean_summary$n <- 1

lakeGeorgeAnnualTemp <- lakeGeorgeSurfMean_summary %>% group_by(year) %>% summarise(surfTemp = mean(surfTemp, na.rm = TRUE), 
                                                                                    surf_do_con = mean(surf_do_con, na.rm = TRUE), 
                                                                                    n = sum(n))

summary(lakeGeorgeAnnualTemp$year) #from 1980 - 2013

#Scatter Plot temp over time
windows()
ggplot(data = lakeGeorgeAnnualTemp) +
  geom_point(aes(x = year, y = surfTemp), color = "red") +
  ylab("Temp (\u00B0C)") +
  xlab("") +
  labs(title = "Lake George Annual Temperature 1980-2013") +
  theme(text = element_text(size = 14), plot.title = element_text(hjust=0.5)) +
  theme_light()

#Surface Temp linear regression to check trend significance
st_lm <- lm(lakeGeorgeAnnualTemp$surfTemp ~ lakeGeorgeAnnualTemp$year)
summary(st_lm) #slope of m = 0.078, r-squared value of 0.4302, and p-value of 2.051e-5


#Scatter Plot and Regression for Temp
windows()
ggplot(data = lakeGeorgeAnnualTemp) +
  geom_point(aes(x = year, y = surfTemp, color = "Surface <= 10m")) +
  geom_smooth(aes(x = year, y = surfTemp), method = lm, se = FALSE, color = "red" ) +
  ylab("Temp (\u00B0C)") +
  xlab("") +
  ylim(15, 30) +
  labs(title = "Lake George Annual Temperature 1980-2013 with Linear Regression") +
  theme(text = element_text(size = 14), plot.title = element_text(hjust = 0.5)) +  
  theme_light() +
  scale_colour_manual(name="", values = c("blue","red"))


#Dissolved Oxygen plot and regression

#DO regression
sdo_lm <- lm(lakeGeorgeAnnualTemp$surf_do_con ~ lakeGeorgeAnnualTemp$year)
summary(sdo_lm) #m = -0.013, r squared value of 0.04775, and p-value of 0.01167 not significant for p <= 0.01

windows()
ggplot(data = lakeGeorgeAnnualTemp) +
  geom_point(aes(x = year, y = surf_do_con, color = "Surface <= 10m")) +
  geom_smooth(aes(x = year, y = surf_do_con), method = lm, se = FALSE, color = "red") +
  labs(title = "Lake George Annual DO 1980-2013 with Linear Regression",
       y = "DO mg/L", x = '') +
  theme_light() +
  theme(text = element_text(size = 14), plot.title = element_text(hjust = 0.5)) +  
  scale_colour_manual(name="", 
                      values = c("blue", "red"))





