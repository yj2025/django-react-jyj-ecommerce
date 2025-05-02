import { getCategories } from '@/api/CategoryApi';
import { getProducts } from '@/api/ProductApi';

import React, { useEffect, useState } from 'react';

const Products = () => {
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('전체');
  //dev_4_Fruit
  const [products, setProducts] = useState([]);

  useEffect(() => {
    //카테고리 가져오기
    getCategories()
      .then((res) => {
        console.log('Categories data:', res.data);
        // 응답이 배열인지 확인하고, 아니면 적절히 변환
        const categoriesData = Array.isArray(res.data)
          ? res.data
          : res.data && typeof res.data === 'object' && res.data.content
          ? res.data.content
          : [];
        setCategories(categoriesData);
      })
      .catch((err) => {
        console.error('Error fetching categories:', err);
        setCategories([]); // 오류 발생 시 빈 배열로 설정
      });

    //상품 불러오기
    getProducts()
      .then((res) => {
        console.log('Products data:', res.data);
        // 응답이 배열인지 확인하고, 아니면 적절히 변환
        const productsData = Array.isArray(res.data)
          ? res.data
          : res.data && typeof res.data === 'object' && res.data.content
          ? res.data.content
          : [];
        setProducts(productsData);
      })
      .catch((err) => {
        console.error('Error fetching products:', err);
        setProducts([]); // 오류 발생 시 빈 배열로 설정
      });
  }, []);

  // API 응답 데이터를 더 안전하게 처리
  const categoriesArray = Array.isArray(categories) ? categories : [];

  const filteredProducts =
    selectedCategory === '전체'
      ? products.filter((p) => p.image != null)
      : products.filter((p) => p.category && p.category.name === selectedCategory && p.image);

  return (
    <>
      {/* Fruits Shop Start*/}
      <div className="container-fluid fruite py-0">
        <div className="container py-5">
          <div className="tab-class text-center">
            <div className="row g-4">
              <div className="col-lg-4 text-start">
                <h1>Our Organic Products</h1>
              </div>
              <div className="col-lg-8 text-end">
                <ul className="nav nav-pills d-inline-flex text-center mb-5">
                  <li className="nav-item">
                    <a
                      className="d-flex m-2 py-2 bg-light rounded-pill active"
                      data-bs-toggle="pill"
                      href="#tab-1"
                      onClick={(e) => {
                        e.preventDefault();
                        setSelectedCategory('전체');
                      }}
                    >
                      <span className="text-dark" style={{ width: 130 }}>
                        {'전체'}
                      </span>
                    </a>
                  </li>
                  {categoriesArray.map((category, index) => (
                    <li className="nav-item" key={index}>
                      <a
                        className="d-flex m-2 py-2 bg-light rounded-pill active"
                        data-bs-toggle="pill"
                        href="#tab-1"
                        onClick={(e) => {
                          e.preventDefault();
                          setSelectedCategory(category.name);
                          console.log('Selected category:', category.name);
                        }}
                      >
                        <span className="text-dark" style={{ width: 130 }}>
                          {category.name}
                        </span>
                      </a>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
            <div className="tab-content">
              <div id="tab-1" className="tab-pane fade show p-0 active">
                <div className="row g-4">
                  <div className="col-lg-12">
                    <div className="row g-4">
                      {/* dev_4_Fruit */}
                      {filteredProducts.map((product, idx) => (
                        <div key={product.id || idx} className="col-md-6 col-lg-4 col-xl-3">
                          <div className="rounded position-relative fruite-item">
                            <div className="fruite-img fruite-img ratio ratio-4x3 overflow-hidden rounded-top">
                              <img
                                src={`${import.meta.env.VITE_API_BASE_URL}${product.image}`}
                                className="img-fluid w-100 rounded-top"
                                alt={product.name || 'Product image'}
                              />
                            </div>
                            <div
                              className="text-white bg-secondary px-3 py-1 rounded position-absolute"
                              style={{ top: 10, left: 10 }}
                            >
                              {product.category && product.category.name ? product.category.name : 'Unknown'}
                            </div>
                            <div className="p-4 border border-secondary border-top-0 rounded-bottom">
                              <h4>{product.name}</h4>
                              <p>
                                Lorem ipsum dolor sit amet consectetur adipisicing elit sed do eiusmod te incididunt
                              </p>
                              <div className="d-flex flex-column justify-content-center align-items-center flex-lg-wrap">
                                <p className="text-dark fs-5 fw-bold mb-2">${product.price} / kg</p>
                                <a href="#" className="btn border border-secondary rounded-pill px-3 text-primary">
                                  <i className="fa fa-shopping-bag me-2 text-primary" /> Add to cart
                                </a>
                              </div>
                            </div>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      {/* Fruits Shop End*/}
    </>
  );
};

export default Products;
