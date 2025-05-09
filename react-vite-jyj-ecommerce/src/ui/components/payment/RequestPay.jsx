const RequestPay = (shippingData, cart=null, pg="kakaopay", pay_method='card') => {
    const impCode = 'imp56131150' // 상태코드

    return new Promise((resolve, reject) => {

        IMP.init(impCode) // 아임포트 가맹점 식별코드

        const data ={
            pg:pg,
            pay_method: payMethod, // 결제수단
            //merchant_uid: payment-${crypto.randomUUID()}, // 주문번호 생성(생략시 포트원에서 자동생성)
            name: "꿈나라 쇼핑몰", // 결제창에 노출될 상품명
            amount: 100,//테스트를 위하여 100원으로 설정
            buyer_email:shippingData.email, //로그인된 유저만 접근할수 있는 페이지 이므로 user객체를 바로 쓸수 있음
            buyer_name: shippingData.full_name, //구매자 이름
            buyer_tel: shippingData.phone,
            buyer_addr: shippingData.address1,
            buyer_postcode: shippingData.zipcode,
        }

        IMP.request_pay(data, async(rsp) => {
            
            if(rsp.success) {

            }else{
                alert(`결제 실패, ${rsp.error_msg}`)
                reject(new Error(rsp.error_msg)) // 결제 실패 
            }
        })
    });
}

export default RequestPay