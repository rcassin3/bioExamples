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



groupWorkDF <- read.csv("For Analaysis group 1.csv")

head(groupWorkDF)
str(groupWorkDF)

groupAvg <- groupWorkDF %>% group_by(Species, Treatment) %>% 
  summarise(meanGroup = mean(Abs), sdGroup = sd(Abs))

unique(groupAvg$Species)
groupAvg$Species <- factor(groupAvg$Species, 
                           levels = c('bkg', 'A. hyd', 'B. sub', 'C.fre',
                                      'E.col', 'P.flu', 'S. epi', 'S. mar'))


windows()
ggplot(data = groupAvg, aes(Species, y = meanGroup, fill = Treatment)) +
  geom_bar(stat = "identity", position = "dodge") +
  theme_minimal() +
  scale_fill_manual(values = c('red', 'blue', 'yellow', 'grey')) +
  theme(text = element_text(size = 19), plot.title = element_text(hjust = 0.5)) +
  geom_errorbar(aes(ymin = meanGroup - sdGroup, ymax = meanGroup + sdGroup), position = "dodge") +
  labs(title = "Bacterial Growth after Treatment" , y = "Bacteria Proxy (Abs)")

res.aov2 <- aov(Abs ~ Treatment + Species, data = groupWorkDF)
summary(res.aov2)

res.aov3 <- aov(Abs ~ Treatment * Species, data = groupWorkDF)
summary(res.aov3)

TukeyHSD(res.aov3)
