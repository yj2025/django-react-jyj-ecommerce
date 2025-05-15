import http from './HttpCommon';

//dev_4_Fruit
// # http://127.0.0.1:8000/api/products/
// # 방식   url                 기능
// # GET  products/            list
// # POST products/            create
// # Get  product/{id}         product
// # PUT  product/{id}       modify product
// # DELETE  product/{id}    delete product
export const getProducts = () => {
  return http.get('/api/products/');
};

export const getProductsPaging = ({
  page = 1,
  search = ""
}) => {

  const params = {
    search
  }

  return http.get('/api/product-list/',{params});
};