# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class FinalProjectItem(Item):
    Name = Field()
    Position = Field()
    Location = Field()
    HighSchool = Field()
    ImgURL = Field()
    Stars = Field()
    Height = Field()
    Weight = Field()
    School = Field()
    FortyTime = Field()
    RivalsRanking = Field()
    PostionRank = Field()
    NationalRank = Field()
    StateRank = Field()
    Year = Field()
