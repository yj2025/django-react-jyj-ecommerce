
import { getCategories } from "@/api/CategoryApi"
import { useShop } from "@/contexts/ShopContext"
import { useEffect, useState } from "react"

//dev_10_Fruit
const Shop = () => {

const {setSearch,products,seting,setCategory} = useShop()
//categories = null
const [categories, setCategories] = useState([])



//동기화 지원 안함
useEffect(  () => {
  //http://localhost:8000/api/categories/  

  getCategories()
  .then( (res) => {
    setCategories(res.data)
    console.log(res.data)
  })  
  .catch(err => console.log(err))

},[])

//"GET /api/product-list/?page=1&search=&ordering=price&category=37&page_size=12 HTTP/1.1"
const handleSearchChange = (event)=>{setSearch(event.target.value)}
const handleOrderingChange = (event)=>{setOrdering(event.target.value)}

const handleCategoryClick =(categoryId) => {setCategory(categoryId)}          

return (
<>
  {/* Single Page Header start */}
  <div className="container-fluid page-header py-5">
    <h1 className="text-center text-white display-6">Shop</h1>
    <ol className="breadcrumb justify-content-center mb-0">
      <li className="breadcrumb-item">
        <a href="#">Home</a>
      </li>
      <li className="breadcrumb-item">
        <a href="#">Pages</a>
      </li>
      <li className="breadcrumb-item active text-white">Shop</li>
    </ol>
  </div>
  {/* Single Page Header End */}
  {/* Fruits Shop Start*/}
  <div className="container-fluid fruite py-5">
    <div className="container py-5">
      <h1 className="mb-4">Fresh fruits shop</h1>
      <div className="row g-4">
        <div className="col-lg-12">
          <div className="row g-4">
            <div className="col-xl-3">
              <div className="input-group w-100 mx-auto d-flex">
                <input
                  type="search"
                  className="form-control p-3"
                  placeholder="keywords"
                  aria-describedby="search-icon-1"
                  onChange={handleSearchChange}
                />
                <span id="search-icon-1" className="input-group-text p-3">
                  <i className="fa fa-search" />
                </span>
              </div>
            </div>
            <div className="col-6" />
            <div className="col-xl-3">
              <div className="bg-light ps-3 py-3 rounded d-flex justify-content-between mb-4">
                <label htmlFor="fruits">정렬 선택:</label>
                <select
                  id="fruits"
                  name="fruitlist"
                  className="border-0 form-select-sm bg-light me-3"
                  form="fruitform"
                  onChange={handleOrderingChange}
                >
                  <option value="volvo">정렬선택</option>
                  <option value="price">가격 낮은순</option>
                  <option value="-price">가격 높은순</option>
                  <option value="id">등록순</option>
                  <option value="-id">최신순</option>                  
                </select>
              </div>
            </div>
          </div>
          <div className="row g-4">
            <div className="col-lg-3">
              <div className="row g-4">
                <div className="col-lg-12">
                  <div className="mb-3">
                    <h4>Categories</h4>
                    <ul className="list-unstyled fruite-categorie">
                      
                      { categories && categories?.map((category, index)=>(
                        
                        <li key={index}>
                           {/* style={{ cursor: 'pointer' }}  // 클릭 가능한 UI */}
                          <div onClick={()=> handleCategoryClick(category.id)}   style={{ cursor: 'pointer' }}  className="d-flex justify-content-between fruite-name">
                            <a href="#" onClick={(e)=> e.preventDefault()}>
                              <i className="fas fa-apple-alt me-2" />
                              {category.name}
                            </a>
                            <span>({category.products.length})</span>
                          </div>
                        </li>
                      ))}                        

                                           
                    </ul>
                  </div>
                </div>
                <div className="col-lg-12">
                  <div className="mb-3">
                    <h4 className="mb-2">Price</h4>
                    <input
                      type="range"
                      className="form-range w-100"
                      id="rangeInput"
                      name="rangeInput"
                      min={0}
                      max={500}
                      defaultValue={0}
                      oninput="amount.value=rangeInput.value"
                    />
                    <output
                      id="amount"
                      name="amount"
                      min-velue={0}
                      max-value={500}
                      htmlFor="rangeInput"
                    >
                      0
                    </output>
                  </div>
                </div>
                <div className="col-lg-12">
                  <div className="mb-3">
                    <h4>Additional</h4>
                    <div className="mb-2">
                      <input
                        type="radio"
                        className="me-2"
                        id="Categories-1"
                        name="Categories-1"
                        defaultValue="Beverages"
                      />
                      <label htmlFor="Categories-1"> Organic</label>
                    </div>
                    <div className="mb-2">
                      <input
                        type="radio"
                        className="me-2"
                        id="Categories-2"
                        name="Categories-1"
                        defaultValue="Beverages"
                      />
                      <label htmlFor="Categories-2"> Fresh</label>
                    </div>
                    <div className="mb-2">
                      <input
                        type="radio"
                        className="me-2"
                        id="Categories-3"
                        name="Categories-1"
                        defaultValue="Beverages"
                      />
                      <label htmlFor="Categories-3"> Sales</label>
                    </div>
                    <div className="mb-2">
                      <input
                        type="radio"
                        className="me-2"
                        id="Categories-4"
                        name="Categories-1"
                        defaultValue="Beverages"
                      />
                      <label htmlFor="Categories-4"> Discount</label>
                    </div>
                    <div className="mb-2">
                      <input
                        type="radio"
                        className="me-2"
                        id="Categories-5"
                        name="Categories-1"
                        defaultValue="Beverages"
                      />
                      <label htmlFor="Categories-5"> Expired</label>
                    </div>
                  </div>
                </div>
                <div className="col-lg-12">
                  <h4 className="mb-3">Featured products</h4>
                  <div className="d-flex align-items-center justify-content-start">
                    <div
                      className="rounded me-4"
                      style={{ width: 100, height: 100 }}
                    >
                      <img
                        src="img/featur-1.jpg"
                        className="img-fluid rounded"
                        alt=""
                      />
                    </div>
                    <div>
                      <h6 className="mb-2">Big Banana</h6>
                      <div className="d-flex mb-2">
                        <i className="fa fa-star text-secondary" />
                        <i className="fa fa-star text-secondary" />
                        <i className="fa fa-star text-secondary" />
                        <i className="fa fa-star text-secondary" />
                        <i className="fa fa-star" />
                      </div>
                      <div className="d-flex mb-2">
                        <h5 className="fw-bold me-2">2.99 $</h5>
                        <h5 className="text-danger text-decoration-line-through">
                          4.11 $
                        </h5>
                      </div>
                    </div>
                  </div>
                  <div className="d-flex align-items-center justify-content-start">
                    <div
                      className="rounded me-4"
                      style={{ width: 100, height: 100 }}
                    >
                      <img
                        src="img/featur-2.jpg"
                        className="img-fluid rounded"
                        alt=""
                      />
                    </div>
                    <div>
                      <h6 className="mb-2">Big Banana</h6>
                      <div className="d-flex mb-2">
                        <i className="fa fa-star text-secondary" />
                        <i className="fa fa-star text-secondary" />
                        <i className="fa fa-star text-secondary" />
                        <i className="fa fa-star text-secondary" />
                        <i className="fa fa-star" />
                      </div>
                      <div className="d-flex mb-2">
                        <h5 className="fw-bold me-2">2.99 $</h5>
                        <h5 className="text-danger text-decoration-line-through">
                          4.11 $
                        </h5>
                      </div>
                    </div>
                  </div>
                  <div className="d-flex align-items-center justify-content-start">
                    <div
                      className="rounded me-4"
                      style={{ width: 100, height: 100 }}
                    >
                      <img
                        src="img/featur-3.jpg"
                        className="img-fluid rounded"
                        alt=""
                      />
                    </div>
                    <div>
                      <h6 className="mb-2">Big Banana</h6>
                      <div className="d-flex mb-2">
                        <i className="fa fa-star text-secondary" />
                        <i className="fa fa-star text-secondary" />
                        <i className="fa fa-star text-secondary" />
                        <i className="fa fa-star text-secondary" />
                        <i className="fa fa-star" />
                      </div>
                      <div className="d-flex mb-2">
                        <h5 className="fw-bold me-2">2.99 $</h5>
                        <h5 className="text-danger text-decoration-line-through">
                          4.11 $
                        </h5>
                      </div>
                    </div>
                  </div>
                  <div className="d-flex justify-content-center my-4">
                    <a
                      href="#"
                      className="btn border border-secondary px-4 py-3 rounded-pill text-primary w-100"
                    >
                      Vew More
                    </a>
                  </div>
                </div>
                <div className="col-lg-12">
                  <div className="position-relative">
                    <img
                      src="img/banner-fruits.jpg"
                      className="img-fluid w-100 rounded"
                      alt=""
                    />
                    <div
                      className="position-absolute"
                      style={{
                        top: "50%",
                        right: 10,
                        transform: "translateY(-50%)"
                      }}
                    >
                      <h3 className="text-secondary fw-bold">
                        Fresh <br /> Fruits <br /> Banner
                      </h3>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className="col-lg-9">
              <div className="row g-4 justify-content-center">                
                { products && products.map( (product) => (

                  <div key={product.id} className="col-md-6 col-lg-6 col-xl-4">
                    <div className="rounded position-relative fruite-item">
                      <div className="fruite-img ratio ratio-4x3 overflow-hidden rounded-top">
                        <img
                          src={`${product.image}`}
                          className="img-fluid w-100 rounded-top"
                          alt=""
                        />
                      </div>
                      <div
                        className="text-white bg-secondary px-3 py-1 rounded position-absolute"
                        style={{ top: 10, left: 10 }}
                      >
                        {product.category.name}
                      </div>
                      <div className="p-4 border border-secondary border-top-0 rounded-bottom">
                        <h4 className="text-center">{product.name}</h4>
                        <p>
                          {product.description}
                        </p>
                        <div className="d-flex justify-content-between flex-lg-wrap">
                          <p className="text-dark fs-5 fw-bold mb-0">
                            ${product.price} 원
                          </p>
                          <a
                            href="#"
                            className="btn border border-secondary rounded-pill px-3 text-primary"
                          >
                            <i className="fa fa-shopping-bag me-2 text-primary" />{" "}
                            Add to cart
                          </a>
                        </div>
                      </div>
                    </div>
                  </div>
                  ))
                }
               





                <div className="col-12">
                  <div className="pagination d-flex justify-content-center mt-5">
                    <a href="#" className="rounded">
                      «
                    </a>
                    <a href="#" className="active rounded">
                      1
                    </a>
                    <a href="#" className="rounded">
                      2
                    </a>
                    <a href="#" className="rounded">
                      3
                    </a>
                    <a href="#" className="rounded">
                      4
                    </a>
                    <a href="#" className="rounded">
                      5
                    </a>
                    <a href="#" className="rounded">
                      6
                    </a>
                    <a href="#" className="rounded">
                      »
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  {/* Fruits Shop End*/}
  {/* Back to Top */}
  <a
    href="#"
    className="btn btn-primary border-3 border-primary rounded-circle back-to-top"
  >
    <i className="fa fa-arrow-up" />
  </a>
  {/* JavaScript Libraries */}
  {/* Template Javascript */}
</>

  )
}

export default Shop