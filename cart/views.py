from django.shortcuts import render,get_object_or_404,redirect

from product.models import Category, Product

# Create your views here.

# Global
cartlist = list() # 購物車列表



def cart_view(request):
    global cartlist
    # goodstitle = cartlist
    grandtotal = 0
    categories = Category.objects.all()

    for item in cartlist:
        grandtotal += float(item[3])

    return render(request, 'cart/cart_view.html',{
        'categories': categories,
        'grandtotal':grandtotal,
        'cartlist': cartlist
    })

def add_to_cart(request, product_id):
    global cartlist
    categories = Category.objects.all()
    product = get_object_or_404(Product, pk=product_id)

    if product:
        # 預設購物車中都沒有相同的商品: 購物車內沒有這個商品，用flag = True 表示
        flag = True
        # 用程式檢查購物車中是否有重複的
        for item in cartlist:
            if product.name == item[0]:
                item[2]=str(int(item[2])+1) # 數量加1
                item[3]=str(float(item[3])+product.total)
                flag=False # 表示商品有相同的，修改數量
                break

        if flag:
            # unit[0]: 商品名稱 unit[1]: 商品單價 unit[2]: 商品數量 unit[3]: 商品總價
            templist = list()
            templist.append(product.name)
            templist.append(str(product.total))
            templist.append('1')
            templist.append(str(product.total))
            cartlist.append(templist)

        request.session['cartlist'] = cartlist
        return redirect('cart_view')

    return render(request, 'product/product_view.html', {
        'categories': categories,
    })

def delete_item(request, item_name):
    global cartlist

    for item in cartlist:
        if item[0]==item_name:
            cartlist.remove(item)
    
    request.session['cartlist'] = cartlist
    return redirect('cart_view')
