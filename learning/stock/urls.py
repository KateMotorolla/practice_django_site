from django.urls import path

from stock.views import stock_list, stock_buy_page, stock_sell_page, stock_buy, stock_sell, account

urlpatterns = [
    path('list/', stock_list, name='list'),
    path('buy-page/<int:pk>/', stock_buy_page, name='buy_page'),  # страница с формой покупки
    path('sell-page/<int:pk>/', stock_sell_page, name='sell_page'),  # страница с формой продажи
    path('buy/<int:pk>/', stock_buy, name='buy'),  # обработка покупки
    path('sell/<int:pk>/', stock_sell, name='sell'),  # обработка продажи
    path('account/', account, name='account')
]


