import React, { createContext, useContext, useEffect, useState } from "react";
import { useAuth } from "./AuthContext";
import { getCarts, mergeCart } from "@/api/CartApi";

//dev_6_Fruits
const CartContext = createContext();
//{
  // "34": {"quantity": 1, "price": "10000.00"}, 
  // "33": {"quantity": 1, "price": "12000.00"}
//}
export const CartProvider = ({ children }) => {
  const [cartItems, setCartItems] = useState({});
  const { user } = useAuth();
  
  //dev_7_Fruit
  const [userCart,setUserCart] = useState(null);

  // 비회원일 때 localStorage 저장
  useEffect(() => {
    if (!user) {
      localStorage.setItem("cart", JSON.stringify(cartItems));
      console.log("🛒 savedCart:", localStorage.getItem("cart"));
    }
  }, [cartItems, user]);

  //로그인시 카트를 병합
  //병합 순서

  useEffect(()=>{
    
    const fetchCart = async ()=>{
        //로그인이 되면
        //로컬에 저장된 카트를 서버로 보내어 서버에서 로컬에 저장된 카트를 병합
        if(user){
            const guestCart = JSON.parse(localStorage.getItem("cart") || "{}");
            try {
                
                if(Object.keys(guestCart).length > 0 ){
                    await mergeCart(localStorage.getItem("cart"))
                    localStorage.removeItem("cart");                    
                }

                //병합 작업이 끝난후 서버에서 카트를 다시 로드함
                loadCart()
                
            } catch (error) {
                console.error("장바구니 병합/불러오기 실패", error);
            }
        }    
    }
    fetchCart()
  },[user])
  
  //장바구니 불러오기
  const loadCart = async () => {
    try {
        const response = await getCarts();

        console.log("카트=========")
        console.log(response)
        // 서버 응답: 배열일 경우 변환
        const cartData = {};
        response.data.cart.forEach((item) => {
            cartData[item.product.id] = {
            quantity: item.quantity,
            price: item.price,
            };
        });

        setCartItems(cartData);
        
        //dev_7_Fruit
        if(user){
          setUserCart(response.data)
        }

    } catch (error) {
        console.error("❌ 장바구니 불러오기 실패", error);
    }
  }


  const getTotalItems = ()=>{
      return Object.values(cartItems).reduce((acc, item) => acc + item.quantity, 0);
  }
  
  // 장바구니 추가
  const addToCart = async (product, quantity = 1) => {
    const productId = product.id;
    const price = product.price;

    if (user) {
      try {
        
      } catch (err) {
        console.error("서버 장바구니 추가 실패", err);
      }
    } else {
      //{
        // "34": {"quantity": 1, "price": "10000.00"}, 
        // "33": {"quantity": 1, "price": "12000.00"}
      //}
      setCartItems((prev) => {
        const existing = prev[productId];
        return {
          ...prev,
          [productId]: {
            price,
            quantity: existing ? existing.quantity + quantity : quantity,
          },
        };
        
      });
    }
  };

  return (
    <CartContext.Provider
      value={{
        userCart, //dev_7_Fruit
        cartItems,
        addToCart,
        getTotalItems,
      }}
    >
      {children}
    </CartContext.Provider>
  );
};

export const useCart = () => useContext(CartContext);