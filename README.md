Database 查詢練習應用 - Database query practice app
===============================
這個app可以用來練習資料庫SELECT的操作，個人鑑於學習資料庫課程時，有時會不清楚書上的範例的結果會得出什麼，

所以做了這個網站，也順便練習SQlite3 和 Python flask 當作後端.

這個應用中的資料庫根據[Fundamentals of Database Systems, Global Edition](http://catalogue.pearsoned.co.uk/educator/product/Fundamentals-of-Database-Systems-Global-Edition/9781292097619.page)的範例建起來的，table的csv檔在table資料夾中有興趣的話可以看看

應用中的範例是根據書上的，根據實驗，有些範例是會跑出錯誤的，不過並不影響運行


Built With
===============================
在這個應用中使用了以下框架、庫:
前端:
*  [Bootstrap4](https://v4-alpha.getbootstrap.com/)
*  [Bootstrap-html-template](https://startbootstrap.com/template-overviews/bare/)
*  [Jquery](https://jquery.com/)
*  [Jquery-ui(autoCompelete)](https://jqueryui.com/)
*  [Jinja2](http://jinja.pocoo.org/docs/2.10/)

後端:
*  [Python3.6](https://www.python.org/downloads/)
*  [Flask](http://flask.pocoo.org/)

資料庫:
*  [SQlite3](https://www.sqlite.org/)

如何使用
==============================
開啟cmd安裝好flask後，在應用根目錄輸入

python app.py

即可開啟local server


注意
==============================
這個應用為了方便管理，所以限制了使用者輸入只能使用SELECT，其他如Database操作都會被過濾掉(如CREATE,DELETE...)。

這個資料庫中的資料皆為虛構，並且資料庫的表格和資料皆屬於[Fundamentals of Database Systems, Global Edition](http://catalogue.pearsoned.co.uk/educator/product/Fundamentals-of-Database-Systems-Global-Edition/9781292097619.page)所有。