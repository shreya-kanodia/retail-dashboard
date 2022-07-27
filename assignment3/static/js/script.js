const totalAmt = document.getElementById('ts');
const saleTable = document.getElementById('table-b');
const avg_sale = document.getElementById('avg_sale');
const unq_visi = document.getElementById('uv');

const base_url = 'http://127.0.0.1:5000';

const getTotal = async () => {
    const requestData = {
        method: "GET",
        mode: 'cors',
        headers: {
            Accept: "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + localStorage.getItem('access_token'),
        },
    }

    const response = await fetch(base_url + '/totalsales', requestData);
    const data = await response.json();
    totalAmt.innerHTML = `${data.total_sales}`;
};

const getAvgSale = async () => {
    const requestData = {
        method: "GET",
        mode: 'cors',
        headers: {
            Accept: "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + localStorage.getItem('access_token'),
        },
    }

    const response = await fetch(base_url + '/avg_sales_per_customer', requestData);
    const data = await response.json();
    avg_sale.innerHTML = `$${data.var}`;
    console.log(data.var);
};
const getUnQVisi = async () => {
    const requestData = {
        method: "GET",
        mode: 'cors',
        headers: {
            Accept: "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + localStorage.getItem('access_token'),
        },
    }

    const response = await fetch(base_url + '/uniquevisitors', requestData);
    const data = await response.json();
    unq_visi.innerHTML = `${data.unique_visitor}`;
};

const getSaleDetails = async () => {
    const requestData = {
        method: "GET",
        mode: 'cors',
        headers: {
            Accept: "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + localStorage.getItem('access_token'),
        },
    }

    const sales = await fetch(base_url + '/daily_sales_list', requestData);
    if (sales.status !== 200) {
        return sales.status;
    }
    const data = await sales.json();

    for (let sale of data.sold_items) {
        saleTable.innerHTML += `
        <tr>
          <td>${sale.product_id}</td>
          <td>${sale.user_id}</td>
          <td>${sale.product_des}</td>
          <td>${sale.sale_amount}</td>
        </tr>
      `
    }
};


getTotal();
getSaleDetails();
getAvgSale();
getUnQVisi();