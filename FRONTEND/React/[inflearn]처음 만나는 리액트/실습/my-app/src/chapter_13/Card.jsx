function Card(props) {
  // 하위 컴포넌트를 감싸서 카드 형태로 보여주는 컴포넌트
  const { title, backgroundColor, children } = props;

  return (
    <div
      // specialization
      style={{
        margin: 8,
        padding: 8,
        borderRadius: 8,
        boxShadow: "0px 0px 4px grey",
        backgroundColor: backgroundColor || "white",
      }}
    >
      {/* 엘리먼트를 조건부로 표현 */}
      {title && <h1>{title}</h1>}
      {/* containment */}
      {children}
    </div>
  );
}

export default Card;