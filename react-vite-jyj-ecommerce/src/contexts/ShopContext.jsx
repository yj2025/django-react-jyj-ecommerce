import { createContext, useContext, useState } from "react"

const ShopContext = createContext()

export const useShop = () => useContext(ShopContext)

export const ShopProvider = ({childaren}) => {

    const [Products, setProducts] = useState([])
    const [search, setSearch] = useState("")

    // 상품 목록 호출

    try {
        const fetchProducts = async () => ({
            search: search,
        })
        
        setProducts(Response.data.results);

    } catch (error) {
        console.error("상품 목록을 불러오는 중 오류 발생:", error)
    }


    
    return <ShopContext.Provider value={'없음'}>{children}</ShopContext.Provider>
}