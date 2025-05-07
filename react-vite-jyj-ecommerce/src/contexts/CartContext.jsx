import { createContext, useEffect, useState } from "react";
import { useAuth } from "./AuthContext";


const CartContext = createContext()

//비로그인을 위한 카트 구성 = 서버 User 모델 old_cart 형식과 맞춤
// {
//     "1":{"quantity":7,"price":"3000.00"}
//     "2":{"quantity":1,"price":"5000.00"}
//  }

export const CartProvider = ({children}) => {
    const [cartItems, setCartItems] = useState({})
    const {user} = useAuth();

    // 비회원 카트를 localStorage 저장
    // cartItems, user 변수에 변화가 생기면, 해당 콜백함수 호출
    useEffect(()=>{
        if(!user){ // 비로그인
            localStorage.setItem("cart",JSON.stringify(cartItems));
        }
    }, [cartItems,user])

    // 장바구니 추가
     const addToCart = (product, quantity=1)=>{
        const productId = product.productId
        const pirce = product.price

        if(user) {

        }else{
            
            setCartItems((prev) => {
                const existing = prev[productId]

                return {
                    ...prev,
                    [productId]:{
                        price,
                        quantity: existing ? existing.quantity + quantity : quantity,
                    }
                };
            });

        }
        
     }

    return <CartContext.Provider value={""}>{children}</CartContext.Provider>
}

export const useCart = () => useContext(CartContext)

