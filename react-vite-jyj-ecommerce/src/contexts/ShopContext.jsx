import { createContext, useContext, useState, useEffect } from "react"

const ShopContext = createContext()

export const useShop = () => useContext(ShopContext)

export const ShopProvider = ({ children }) => {
    const [products, setProducts] = useState([])
    const [search, setSearch] = useState("")
    const [currentPage, setCurrentPage] = useState(1)

    // 상품 목록 호출 함수
    const fetchProducts = async () => {
        try {
            // 예시: API 요청
            const response = await fetch(`/api/products?page=${currentPage}&search=${search}`)
            const data = await response.json()
            setProducts(data.results)
        } catch (error) {
            console.error("상품 목록을 불러오는 중 오류 발생:", error)
        }
    }

    // 컴포넌트 처음 마운트될 때 한 번 호출
    useEffect(() => {
        fetchProducts()
    }, [search, currentPage])

    return (
        <ShopContext.Provider value={{ products, search, setSearch, currentPage, setCurrentPage }}>
            {children}
        </ShopContext.Provider>
    )
}