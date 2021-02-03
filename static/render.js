const router = async () => {
  const header = document.getElementById('header-container');
  header.innerHTML = await Header.render();
};

render: async () => {
// 응답으로 얻은 JSON 데이터
// const results = await파이썬에서 응답한 변수 값 
return `
  <div class="form-container">
    <table>
      <thead>
        <th>코드</th>
        <th>상품명</th>
        <th>컬러</th>
        <th>사이즈</th>
        <th>가격</th>
      </thead>
      <tbody id='table'>
      ${results.map(result => `
        <tr id="row">
          <td>${result.code}</td>
          <td>${result.name}</td>
          <td>${result.color}</td>
          <td>${result.size}</td>
          <td>${result.price}</td>
        </tr>
        `
        )}
      </tbody>
    </table>  
  </div>
`
};