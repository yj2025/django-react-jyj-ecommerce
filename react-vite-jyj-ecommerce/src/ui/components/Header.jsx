import { Outlet } from "react-router-dom"
import heroImg1 from '@/assets/fruits/img/hero-img-1.png'
import heroImg2 from '@/assets/fruits/img/hero-img-2.jpg'
import { useAuth } from "@/contexts/AuthContext"
import { Link } from 'react-router-dom';
import { useCart } from "@/contexts/CartContext";

//dev_2_fruit
const Header = () => {

  //dev_5_Fruit
  const{user,logout} = useAuth();
  console.log(user)

  const logoutHandle = () =>{
    logout()
  }

  //dev_6_Fruit 장바구니 카트 숫자
  const { getTotalItems} = useCart()

return (
        <>
  {/* Spinner Start */}
  {/* <div
    id="spinner"
    className="show w-100 vh-100 bg-white position-fixed translate-middle top-50 start-50  d-flex align-items-center justify-content-center"
  >
    <div className="spinner-grow text-primary" role="status" />
  </div> */}
  {/* Spinner End */}
  {/* Navbar start */}
  <div className="container-fluid fixed-top">
    <div className="container topbar bg-primary d-none d-lg-block">
      <div className="d-flex justify-content-between">
        <div className="top-info ps-2">
          <small className="me-3">
            <i className="fas fa-map-marker-alt me-2 text-secondary" />{" "}
            <a href="#" className="text-white">
              123 Street, New York
            </a>
          </small>
          <small className="me-3">
            <i className="fas fa-envelope me-2 text-secondary" />
            {/* dev_5_Fruit */}
            {user ? (
                  <span
                    className="text-white"
                    style={{ cursor: "pointer" }}
                    onClick={logoutHandle}
                  >
                    {user.username}님 환영합니다.
                  </span>
                ) : (
                  <Link to="/login" className="text-white">로그인을 해주세요</Link>
            )}

          </small>
        </div>
        <div className="top-link pe-2">
          <a href="#" className="text-white">
            <small className="text-white mx-2">Privacy Policy</small>/
          </a>
          <a href="#" className="text-white">
            <small className="text-white mx-2">Terms of Use</small>/
          </a>
          <a href="#" className="text-white">
            <small className="text-white ms-2">Sales and Refunds</small>
          </a>
        </div>
      </div>
    </div>
    <div className="container px-0">
      <nav className="navbar navbar-light bg-white navbar-expand-xl">
        <Link to="/" className="navbar-brand">
          <h1 className="text-primary display-6">Fruitables</h1>
        </Link>
        <button
          className="navbar-toggler py-2 px-3"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarCollapse"
        >
          <span className="fa fa-bars text-primary" />
        </button>
        <div className="collapse navbar-collapse bg-white" id="navbarCollapse">
          <div className="navbar-nav mx-auto">
            <Link to = "/" className="nav-item nav-link active">
              Home
            </Link>
            <Link to ="/shop" className="nav-item nav-link">
              Shop
            </Link>
            <a href="shop-detail.html" className="nav-item nav-link">
              Shop Detail
            </a>
            <div className="nav-item dropdown">
              <a
                href="#"
                className="nav-link dropdown-toggle"
                data-bs-toggle="dropdown"
              >
                Pages
              </a>
              <div className="dropdown-menu m-0 bg-secondary rounded-0">
                <Link to="/cart" className="dropdown-item">
                  Cart
                </Link>
                <a href="chackout.html" className="dropdown-item">
                  Chackout
                </a>
                <a href="testimonial.html" className="dropdown-item">
                  Testimonial
                </a>
                <a href="404.html" className="dropdown-item">
                  404 Page
                </a>
              </div>
            </div>
            <a href="contact.html" className="nav-item nav-link">
              Contact
            </a>
          </div>
          <div className="d-flex m-3 me-0">
            <button
              className="btn-search btn border border-secondary btn-md-square rounded-circle bg-white me-4"
              data-bs-toggle="modal"
              data-bs-target="#searchModal"
            >
              <i className="fas fa-search text-primary" />
            </button>
            {/* dev_7_Fruit */}
            <Link to="/cart" className="position-relative me-4 my-auto">
              <i className="fa fa-shopping-bag fa-2x" />
              <span
                className="position-absolute bg-secondary rounded-circle d-flex align-items-center justify-content-center text-dark px-1"
                style={{ top: "-5px", left: 15, height: 20, minWidth: 20 }}
              >
                {/* dev_6_Fruit */}
                {getTotalItems()}
              </span>
            </Link>
            <a href="#" className="my-auto">
              <i className="fas fa-user fa-2x" />
            </a>
          </div>
        </div>
      </nav>
    </div>
  </div>
  {/* Navbar End */}
  {/* Modal Search Start */}
  <div
    className="modal fade"
    id="searchModal"
    tabIndex={-1}
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div className="modal-dialog modal-fullscreen">
      <div className="modal-content rounded-0">
        <div className="modal-header">
          <h5 className="modal-title" id="exampleModalLabel">
            Search by keyword
          </h5>
          <button
            type="button"
            className="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          />
        </div>
        <div className="modal-body d-flex align-items-center">
          <div className="input-group w-75 mx-auto d-flex">
            <input
              type="search"
              className="form-control p-3"
              placeholder="keywords"
              aria-describedby="search-icon-1"
            />
            <span id="search-icon-1" className="input-group-text p-3">
              <i className="fa fa-search" />
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
  {/* Modal Search End */}

</>

  
    )
}

export default Header