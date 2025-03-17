@router.get('/', response_model=schema.Showarticle)
def all_articles(db: Session = Depends(get_db)):
    return article.get_all(db)

@router.get('/{article_id}', status_code=status.HTTP_200_OK, response_model=schema.Showarticle)
def show_article(article_id: int, db: Session = Depends(get_db)):
    return article.show_article(article_id, db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(articles: schema.ArticleBase, db: Session = Depends(get_db)):
    return article.create(articles, db)

@router.put('/{article_id}', status_code=status.HTTP_202_ACCEPTED)
def update_article(article_id: int, articles: schema.ArticleBase, db: Session = Depends(get_db)):
    return article.update(article_id, articles, db)

@router.delete('/{article_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_article(article_id: int, db: Session = Depends(get_db)):
    return article.delete(article_id, db)