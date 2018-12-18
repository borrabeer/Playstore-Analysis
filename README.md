# Playstore-Analysis
## PSIT 2018 Project about Google Playstore Analysis
https://borrabeer.github.io/Playstore-Analysis/

 Playstore-Analysis คือโปรเจคในวิชา Problem Solving Information Technology หรือ PSIT. โดยโปรเจคนี้เป็นโปรเจคเกี่ยวกับการนำข้อมูลมาวิเคราะห์ออกมาเป็นกราฟโดยใช้เครื่องมือต่างๆ ในภาษา Python ในการทำโปรเจคครั้งนี้้

การทำโปรแกรมนี้เพื่อฝึกหาข้อมูลและการทำงานเป็นทีม ฝึกด้านโปรแกรมมิ่ง การใช้ pandas และ pygal
-	Pandas(PANel DAta)  เป็น Library ใน Python ที่ทำให้เราเล่นกับข้อมูลได้ง่ายขึ้น เหมาะมากสำหรับทำ Data Cleaning / Wrangling
-	Pygal เป็น module หนึ่งใน python ในการสร้างแผนภูมิ โดยไฟล์แผนภูมิเป็นรูปแบบ svg

จากการทำโปรเจคครั้งนี้เราได้นำ data ของ Google Playstore มาจากเว็บ <a href="https://www.kaggle.com/lava18/google-play-store-apps?fbclid=IwAR1JLYzlbAIL-DrILa112YFNPZuSOeGj9bTPz5gb1MFEQkealmPB1V7mUHY">kaggle</a> โดย data ที่เราได้มานั้นจะเป็นไฟล์ .csv ซึ่งจะมีข้อมูลหลายหัวข้อให้เราได้เลือกใช้ดังนี้
- App
- Category
- Rating
- Reviews
- Size
- Installs
- Type
- Price
- Content Rating
- Genres

โดยเราได้นำ data ที่ได้มานั้นมาวิเคราะห์ในหัวข้อต่างๆดังนี้
- <b>Rating</b>
- <b>Review</b>
- <b>Size</b>
- <b>Install</b>

## Rating
คือ หัวข้อที่เรานำยอด Rating ของแอพพลิเคชั่นใน Google Playstore มาหาค่าเฉลี่ยของแต่ละ category หรือหมวดหมู่ของแอพพลิเคชั่นนั้นๆ
โดยจากเกณฑ์การให้คะแนนเป็นช่วง 0-5

## Review
คือ การนำยอดจำนวนครั้งของการีวิวในแต่ละแอพพลิเคชั่นมาหาค่าเฉลี่ยว่าในแต่ละ category นั้นหมวดหมู่ใดมีจำนวนการรีวิวมากที่สุดรวมถึงทั้งด้านบวกและด้านลบ
ซึ่งเราได้ทำการวิเคราะห์ออกมาเป็นกราฟ

## Size
คือ การนำขนาดของแต่ละแอพพลิเคชั่นมาวิเคราะห์ว่าในแต่ละแอพพลิเคชั่นนั้นจะมีขนาดในหมวด category ใดที่มีขนาดใหญ่ที่สุดซึ่งเราแบ่งออกเป็นแต่ละ category

## Install
หรือ Most Install เป็นการหายอดดาวน์โหลดสูงสุดใน Google Playstore ซึ้งจาก data ที่เราได้นำมาใช้นั้นสังเกตุได้ว่า data Install นั้นจะให้มาเป็นช่วงของตัวเลขซึ่งเราได้วิเคราะห์ออกมาได้ว่ามี แอพพลิเคชั่นที่มียอดดาวน์โหลดสูงสุดทั้งหมด 20 รายการซึ่งมียอดดาวน์โหลดอยู่ที่ 1,000,000,000+ ครั้ง

## Members
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="docs/img/members/member1.jpg" width="100px"  height="100">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href=""><img src="docs/img/members/member2.jpg" width="100px"  height="100"></a> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href=""><img src="docs/img/members/member3.jpg" width="100px"  height="100"></a> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href=""><img src="docs/img/members/member4.jpg" width="100px"  height="100"></a> 

- 61070032 นาย ชนกันต์ สุดตาธรรม [Chanakan32](https://github.com/Chanakan32)
- 61070133 นาย พอพล อินทรีย์ [DoubleR0](https://github.com/DoubleR0)
- 61070198 นาย วรพัฒน์ ปักกาเวสา [Borrabeer](https://github.com/borrabeer)
- 61070226 นาย ศุภพัฒน์ ภูริวิทย์วัฒนา [Supapatfirst](https://github.com/Supapatfirst)
