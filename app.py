from flask import Flask
from views import html

app = Flask(__name__)

app.add_url_rule("/", 'home', html.home)
app.add_url_rule("/menu", 'menu', html.menu)
app.add_url_rule("/contact_us", 'contact_us', html.contact_us, methods=['GET', 'POST'])
app.add_url_rule("/about_us", 'about_us', html.about_us)

app.add_url_rule("/cashier/orders", 'order_list', html.order_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)
