from . import marketplace_bp
import decorators
import marketplace_backend
from flask import render_template, jsonify, request, redirect, url_for, session
import generators


@marketplace_bp.route('/marketplace', methods=['GET'])
@decorators.user_login_checker
@decorators.handle_errors
def shop():
    catalogue = marketplace_backend.catalogue_generator()
    today_deals = marketplace_backend.today_deals()
    return render_template('marketplace/shop.html', catalogue=catalogue, today_deal=today_deals)


@marketplace_bp.route('/modal-product-details/<product_id>', methods=['GET'])
def modal_product_details(product_id):
    result_set = marketplace_backend.modal_product_details(product_id)
    return jsonify(result_set)


@marketplace_bp.route('/product-details/', methods=['GET'])
@decorators.user_login_checker
@decorators.handle_errors
def product_details():
    return render_template('marketplace/product-details.html')


@marketplace_bp.route('/cart', methods=['GET'])
@decorators.user_login_checker
@decorators.handle_errors
def cart():
    catalogue = marketplace_backend.catalogue_generator()
    return render_template('marketplace/cart.html', catalogue=catalogue, back=request.referrer)


@marketplace_bp.route('/checkout', methods=['GET', 'POST'])
@decorators.user_login_checker
@decorators.handle_errors
def checkout():
    if request.method == "POST":
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        phone_number = generators.phone_num_checker(request.form['phone-number'])
        street_address = request.form['street-address']
        building = request.form['building']
        town = request.form['town']
        state = town
        order_notes = request.form['order-notes']
        gift_message = request.form['gift-message']
        orders_details = request.form.getlist('cart')
        payment_method = request.form.get('payment-group')
        payment_status = "Not Paid"
        amount = orders_details[-1]
        payment_number = generators.phone_num_checker(request.form['payment-number'])
        orders_details = orders_details[:-1]
        products_ordered = len(orders_details)

        affiliate_id = 0
        if 'affiliate-id' in session:
            affiliate_id = session['affiliate-id']

        result_set = marketplace_backend.user_checkout_section(affiliate_id, first_name, last_name, phone_number,
                                                        street_address, building, town, state, order_notes,
                                                        gift_message, orders_details, payment_method,
                                                        payment_status, amount, payment_number, products_ordered)

        if result_set is None:
            return redirect(url_for('error_log'))
        return redirect(url_for('order_success'))
    else:
        catalogue = marketplace_backend.catalogue_generator()
        return render_template('marketplace/checkout.html', catalogue=catalogue)


@marketplace_bp.route('/order-success/<order_id>', methods=['GET'])
@decorators.user_login_checker
@decorators.handle_errors
def order_success(order_id):
    catalogue = marketplace_backend.catalogue_generator()
    result_set = marketplace_backend.order_success(order_id)
    return render_template('marketplace/order-success.html', catalogue=catalogue, orders=result_set)


@marketplace_bp.route('/order-tracking/<tracking_code>', methods=['GET'])
@decorators.user_login_checker
@decorators.handle_errors
def order_tracking(tracking_code):
    return render_template('marketplace/track-order.html', tracking_code=tracking_code)
