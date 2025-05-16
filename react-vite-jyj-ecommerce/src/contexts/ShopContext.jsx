import { getProducts, getProductsPaging } from "@/api/ProductApi"
import { createContext, useContext, useEffect, useState } from "react"

  //dev_10_Fruit
const ShopContext = createContext()

export const useShop = () => useContext(ShopContext)

export const ShopProvider = ({children}) => {

  // 정렬,페이징, 카테고리 분류된 상품들
  const [products,setProducts] = useState([])
  //검색 관련
  const [search,setSearch] = useState("")
  //정렬 관련
  const [ordering,setOrdering] = useState("")
  //카테고리 분류
  const [category,setCategory] = useState("")
  //paging관련 
  const [currentPage,setCurrentPage] = useState(1)
  const [totalCount,setTotalCount] = useState(0)
  
  //min max 필터링
  const [minPrice, setMinPrice] = useState(0);
  const [maxPrice, setMaxPrice] = useState(null);
 

  const fetchProducsts = async () =>{
    
    try {
      const resonse = await getProductsPaging({
        page : currentPage,
        search,
        ordering,
        category,
        min_price : minPrice,
        max_price : maxPrice,        

      })
      console.log(resonse.data)
      setProducts(resonse.data.results);
      setTotalCount(resonse.data.count);
    
    } catch (error) {
      console.error("상품 목록을 불러오는 중 오류 발생:", error);
    }
  }

  //조건이 변경될때 마다 API 다시 호출
  useEffect(()=>{
      fetchProducsts()
  },[currentPage,search,ordering,category,minPrice,maxPrice])

  const value = {
    search,
    setSearch,
    currentPage,
    setCurrentPage,
    totalCount,
    products,
    setProducts,
    ordering,
    setOrdering,
    category,
    setCategory,
    setMinPrice,
    setMaxPrice
  }

  return <ShopContext.Provider value={value}>{children}</ShopContext.Provider>
}