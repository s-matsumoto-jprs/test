package jp.co.jprs;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.URL;
import java.net.URLConnection;
import java.util.Properties;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import net.sf.ehcache.Cache;
import net.sf.ehcache.CacheManager;
import net.sf.ehcache.Element;
import org.apache.log4j.Logger;

/**
 * Servlet implementation class Controller
 */
public class AuthenticationAgency extends HttpServlet {
    /** クラスバージョン */
    private static final long serialVersionUID = 1L;

    /** ロガー */
    private static final Logger LOG =
            Logger.getLogger(AuthenticationAgency.class.getName());

    /** キャッシュ */
    private static CacheManager manager = CacheManager.getInstance();

    /** 認証局URL */
    private static String authServiceUrl;

    /** キャッシュ名 */
    private static final String CACHE_NAME = "AuthenticationServiceCache";

    /** propertiesファイル キー名: 認証局URL */
    private static final String PROP_URL = "authentication.url";

    /** propertiesファイル キー名: キャッシュリクエスト  */
    private static final String PROP_CHACHE_REQUEST = "cache.request";

    /** キャッシュリクエストリスト */
    private String[] cacheRequestList;

    /** propertiesファイル セパレータ */
    public static final String PROP_SEPATRATOR = ",";

    /**
     * @return
     * @see HttpServlet#HttpServlet()
     */
    public AuthenticationAgency() {
        super();
    }

    /**
     * 初期化
     *
     * @exception ServletException システム異常
     */
    public void init() throws ServletException {
        Properties prop = new Properties();
        // property ファイル読み込み
        try {
            prop.load(this.getClass().getResourceAsStream("/agency.properties"));
        } catch (Exception e) {
            LOG.fatal("設定ファイル読込失敗", e);
            throw new ServletException(e);
        }

        if (prop.containsKey(PROP_URL) && prop.containsKey(PROP_CHACHE_REQUEST)) {
            authServiceUrl = prop.getProperty(PROP_URL);
            cacheRequestList = prop.getProperty(PROP_CHACHE_REQUEST).split(PROP_SEPATRATOR);
        } else {
            LOG.fatal("設定ファイルの必須項目が見つかりません");
            throw new ServletException();
        }

        LOG.info(" URL : " + authServiceUrl);
        LOG.info(" start");
    }

    /**
     * 終了処理
     */
    public void destroy() {
        manager.shutdown();
        LOG.info(" stop");
    }

    /**
     * GETメソッドの実装
     *
     * @param request リクエスト
     * @param response レスポンス
     * @exception ServletException システム異常
     */
    protected void doGet(HttpServletRequest request,
            HttpServletResponse response) throws ServletException, IOException {
        // 何もしない
    }

    /**
     * POSTメソッドの実装
     *
     * @param request リクエスト
     * @param response レスポンス
     * @exception ServletException システム異常
     */
    protected void doPost(HttpServletRequest request,
            HttpServletResponse response) throws ServletException, IOException {
        try {
            // soapのbody部を取得
            BufferedReader in = new BufferedReader(
                    new InputStreamReader(request.getInputStream(), "UTF-8"));

            String reqLine = null;
            String cliRequest = "";
            while ((reqLine = in.readLine()) != null) {
                cliRequest += reqLine;
            }

            // bodyをkeyにキャッシュから取得
            Cache cache = manager.getCache(CACHE_NAME);
            Element element = cache.get(cliRequest);

            if (element == null) {
                // キャッシュになければ認証サーバーに問い合わせ
                URL authenticationServiceURL = new URL(authServiceUrl);

                URLConnection con = authenticationServiceURL.openConnection();
                con.setDoOutput(true);

                // body部分をリクエストへ書き込む
                OutputStreamWriter ow = new OutputStreamWriter(
                        con.getOutputStream());
                BufferedWriter bw = new BufferedWriter(ow);
                bw.write(cliRequest);

                bw.close();
                ow.close();

                //  認証サーバからの応答のbody部分を取得し、レスポンスへ書き込む
                InputStreamReader ir = new InputStreamReader(
                        con.getInputStream(), "UTF-8");
                BufferedReader br = new BufferedReader(ir);

                String resLine = null;
                String authResponse = "";
                while((resLine = br.readLine()) != null) {
                    authResponse += resLine;
                }
                response.setContentType("text/xml; charset=UTF-8");
                response.getWriter().write(authResponse);

                // リクエスト内に指定アクション名が含まれている場合のみキャッシュに保存
                for (String requestName : cacheRequestList) {
                    if (cliRequest.indexOf(requestName) != -1) {
                      // 認証サーバからの応答のheaderとbody部分を保存
                      CacheObject cacheObjectToCache = new CacheObject();
                      cacheObjectToCache.setBody(authResponse);
                      cache.put(new Element(cliRequest, cacheObjectToCache));
                    }
                }
            } else {
                // キャッシュからオブジェクトを取得
                CacheObject cacheObjectFromCache = (CacheObject)element.getObjectValue();

                // キャッシュからbody を取得
                String cacheResponse = cacheObjectFromCache.getBody();

                //response へ body をセット
                response.setContentType("text/xml; charset=UTF-8");
                response.getWriter().write(cacheResponse);
            }
        } catch (Exception e) {
            LOG.fatal("例外が発生しました", e);
        }
    }
}
