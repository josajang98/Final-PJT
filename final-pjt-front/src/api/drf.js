const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const ARTICLES = 'articles/'
const COMMENTS = 'comments/'


const BASE_URL = 'https://api.themoviedb.org/3/'
const api_key = 'ad488474335fabb016f15ea2b4edaaba'
const language = 'ko-KR'
export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },
  articles: {
    // /articles/
    articles: () => HOST + ARTICLES,
    // /articles/1/
    article: articlePk => HOST + ARTICLES + `${articlePk}/`,
    likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
    comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
    comment: (articlePk, commentPk) =>
      HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,
  },
  tmdb: {
    nowPlaying: () => BASE_URL + `movie/now_playing/?api_key=${api_key}&language=${language}`,
    popular: (page) => BASE_URL + `movie/popular/?api_key=${api_key}&language=${language}&page=${page}`,
    searchPerson: (query) => BASE_URL + `search/person/?api_key=${api_key}&language=${language}&query=${query}`,
    person: (person_id) => BASE_URL + `person/${person_id}/movie_credits?api_key=${api_key}&language=${language}`,
    credits: (movie_id) => BASE_URL + `movie/${movie_id}/credits/?api_key=${api_key}&language=${language}`,
  },
}
