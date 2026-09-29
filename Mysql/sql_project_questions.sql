use jeevan_raksha_pharmacy;
-- q1. retrive the name and city of all customers
select name,city from customers


-- q2.find the names of medicines

select name,category from medicines where category IN ('syrup','injection');

-- q3.list all orders where the total amount greater than 500
select * from orders where total_amount >500;

-- q4.find the phones of all customers living in mumbai
select name,phone from customers where city='mumbai';

-- q5. count how many orders are paid using upi
select count(*) as upi_orders  from orders where payment_mode='upi';

-- q6. count how many medicines by apollo distributors

select count(m.medicine_id) as count_medicines from medicines m 
join suppliers s 
on m.supplier_id=s.supplier_id 
where s.supplier_name='Apollo Distributors';


 -- q7.  list the customername order date and total amount for every order
 select c.name as customer_name,o.order_date,o.total_amount
 from orders o join customers c on c.customer_id=o.customer_id;
 
 -- q8. revenue by payment mode
 select payment_mode,sum(total_amount) as revenue from orders group by payment_mode;
 
 -- q9find the best selling medicine
 select m.name,sum(oi.quantity) as total_qty from order_items oi
 join medicines m on oi.medicine_id=m.medicine_id
 group by m.name
 order by total_qty desc limit 1;

-- q10. customers who spend more than 1000
select c.name, sum(o.total_amount) as total_spent from customers c
join orders o
on o.customer_id=c.customer_id
group by c.name
having total_spent> 1000;

-- q11. medicine name,stock quantity, supplier_name
-- for medicines with less than 50 units left in the stock

select m.name as medicine_name,m.stock_quantity, s.supplier_name
from medicines m
join suppliers s
on m.supplier_id = s.supplier_id
where m.stock_quantity <=50;
  