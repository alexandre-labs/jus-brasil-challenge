# fmt: off
DATA = """











<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>






























































<head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />










        <script language="javascript" type="text/JavaScript" src="https://esaj.tjsp.jus.br/sajcas/verificarLogin.js?script=1558158237842"></script>

        <script language="javascript">
                if(window.sajcas && window.sajcas.usuarioLogadoNoCasServer) {
                        var urlRetornoSistema = '';
                        if(urlRetornoSistema === '') {
                                urlRetornoSistema = window.location.href;
                        }

                        if(urlRetornoSistema.lastIndexOf('?') != -1) {
                                urlRetornoSistema += '&';
                        } else {
                                urlRetornoSistema += '?';
                        }
                        urlRetornoSistema+= 'gateway=true';
                        window.location.href = urlRetornoSistema;
                }
        </script>


        <title>Portal de Serviços e-SAJ</title>
































<!-- Includes do spw -->

<script type="text/javascript">window.NREUM||(NREUM={}),__nr_require=function(e,n,t){function r(t){if(!n[t]){var o=n[t]={exports:{}};e[t][0].call(o.exports,function(n){var o=e[t][1][n];return r(o||n)},o,o.exports)}return n[t].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<t.length;o++)r(t[o]);return r}({1:[function(e,n,t){function r(){}function o(e,n,t){return function(){return i(e,[c.now()].concat(u(arguments)),n?null:this,t),n?void 0:this}}var i=e("handle"),a=e(3),u=e(4),f=e("ee").get("tracer"),c=e("loader"),s=NREUM;"undefined"==typeof window.newrelic&&(newrelic=s);var p=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],d="api-",l=d+"ixn-";a(p,function(e,n){s[n]=o(d+n,!0,"api")}),s.addPageAction=o(d+"addPageAction",!0),s.setCurrentRouteName=o(d+"routeName",!0),n.exports=newrelic,s.interaction=function(){return(new r).get()};var m=r.prototype={createTracer:function(e,n){var t={},r=this,o="function"==typeof n;return i(l+"tracer",[c.now(),e,t],r),function(){if(f.emit((o?"":"no-")+"fn-start",[c.now(),r,o],t),o)try{return n.apply(this,arguments)}catch(e){throw f.emit("fn-err",[arguments,this,e],t),e}finally{f.emit("fn-end",[c.now()],t)}}}};a("actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(e,n){m[n]=o(l+n)}),newrelic.noticeError=function(e,n){"string"==typeof e&&(e=new Error(e)),i("err",[e,c.now(),!1,n])}},{}],2:[function(e,n,t){function r(e,n){if(!o)return!1;if(e!==o)return!1;if(!n)return!0;if(!i)return!1;for(var t=i.split("."),r=n.split("."),a=0;a<r.length;a++)if(r[a]!==t[a])return!1;return!0}var o=null,i=null,a=/Version\/(\S+)\s+Safari/;if(navigator.userAgent){var u=navigator.userAgent,f=u.match(a);f&&u.indexOf("Chrome")===-1&&u.indexOf("Chromium")===-1&&(o="Safari",i=f[1])}n.exports={agent:o,version:i,match:r}},{}],3:[function(e,n,t){function r(e,n){var t=[],r="",i=0;for(r in e)o.call(e,r)&&(t[i]=n(r,e[r]),i+=1);return t}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],4:[function(e,n,t){function r(e,n,t){n||(n=0),"undefined"==typeof t&&(t=e?e.length:0);for(var r=-1,o=t-n||0,i=Array(o<0?0:o);++r<o;)i[r]=e[n+r];return i}n.exports=r},{}],5:[function(e,n,t){n.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],ee:[function(e,n,t){function r(){}function o(e){function n(e){return e&&e instanceof r?e:e?f(e,u,i):i()}function t(t,r,o,i){if(!d.aborted||i){e&&e(t,r,o);for(var a=n(o),u=v(t),f=u.length,c=0;c<f;c++)u[c].apply(a,r);var p=s[y[t]];return p&&p.push([b,t,r,a]),a}}function l(e,n){h[e]=v(e).concat(n)}function m(e,n){var t=h[e];if(t)for(var r=0;r<t.length;r++)t[r]===n&&t.splice(r,1)}function v(e){return h[e]||[]}function g(e){return p[e]=p[e]||o(t)}function w(e,n){c(e,function(e,t){n=n||"feature",y[t]=n,n in s||(s[n]=[])})}var h={},y={},b={on:l,addEventListener:l,removeEventListener:m,emit:t,get:g,listeners:v,context:n,buffer:w,abort:a,aborted:!1};return b}function i(){return new r}function a(){(s.api||s.feature)&&(d.aborted=!0,s=d.backlog={})}var u="nr@context",f=e("gos"),c=e(3),s={},p={},d=n.exports=o();d.backlog=s},{}],gos:[function(e,n,t){function r(e,n,t){if(o.call(e,n))return e[n];var r=t();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,n,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return e[n]=r,r}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],handle:[function(e,n,t){function r(e,n,t,r){o.buffer([e],r),o.emit(e,n,t)}var o=e("ee").get("handle");n.exports=r,r.ee=o},{}],id:[function(e,n,t){function r(e){var n=typeof e;return!e||"object"!==n&&"function"!==n?-1:e===window?0:a(e,i,function(){return o++})}var o=1,i="nr@id",a=e("gos");n.exports=r},{}],loader:[function(e,n,t){function r(){if(!E++){var e=x.info=NREUM.info,n=l.getElementsByTagName("script")[0];if(setTimeout(s.abort,3e4),!(e&&e.licenseKey&&e.applicationID&&n))return s.abort();c(y,function(n,t){e[n]||(e[n]=t)}),f("mark",["onload",a()+x.offset],null,"api");var t=l.createElement("script");t.src="https://"+e.agent,n.parentNode.insertBefore(t,n)}}function o(){"complete"===l.readyState&&i()}function i(){f("mark",["domContent",a()+x.offset],null,"api")}function a(){return O.exists&&performance.now?Math.round(performance.now()):(u=Math.max((new Date).getTime(),u))-x.offset}var u=(new Date).getTime(),f=e("handle"),c=e(3),s=e("ee"),p=e(2),d=window,l=d.document,m="addEventListener",v="attachEvent",g=d.XMLHttpRequest,w=g&&g.prototype;NREUM.o={ST:setTimeout,SI:d.setImmediate,CT:clearTimeout,XHR:g,REQ:d.Request,EV:d.Event,PR:d.Promise,MO:d.MutationObserver};var h=""+location,y={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1123.min.js"},b=g&&w&&w[m]&&!/CriOS/.test(navigator.userAgent),x=n.exports={offset:u,now:a,origin:h,features:{},xhrWrappable:b,userAgent:p};e(1),l[m]?(l[m]("DOMContentLoaded",i,!1),d[m]("load",r,!1)):(l[v]("onreadystatechange",o),d[v]("onload",r)),f("mark",["firstbyte",u],null,"api");var E=0,O=e(5)},{}]},{},["loader"]);</script><link rel="stylesheet" href="/cposg/css/spw/spwConcatenado.css" type="text/css"/>
<link rel="stylesheet" href="/cposg/css/esaj.css" type="text/css"/>
<link rel="stylesheet" href="/cposg/css/saj/saj-captcha.css" type="text/css"/>
<link rel="stylesheet" href="/cposg/css/saj/saj-popup-modal.css" type="text/css"/>
<link rel="stylesheet" href="/cposg/css/cpo.css" type="text/css"/>
<link rel="stylesheet" href="/cposg/css/formulario.css" type="text/css"/>
<link rel="stylesheet" href="/cposg/css/tarjaDoProcesso.css" type="text/css"/>

<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />

<script language="javascript" type="text/JavaScript" src="/cposg/js/jquery/jquery.min.js?n=076f8f8e-9d15-4655-ba07-20a605885ee8"></script>
<script language="javascript" type="text/JavaScript" src="/cposg/js/jquery/jquery.func_toggle.js?n=9f90b971-1ec2-4ebc-800f-14790936969c"></script>
<script language="javascript" type="text/JavaScript" src="/cposg/js/jquery/jquery.blockUI.min.js?n=b8959ba9-d962-4632-a874-438d778323dc"></script>
<script language="javascript" type="text/javascript" src="/cposg/js/jquery/jquery.browser.min.js?n=b1cc040c-a404-4349-bbbb-52e626c176ba"></script>
<script language="javascript" type="text/JavaScript" src="/cposg/js/saj/saj-web-2.2.41-4.js?n=162352e4-e7c7-433d-8e63-b2a3797b9fac"></script>
<script language="javascript" type="text/JavaScript" src="/cposg/js/saj/saj-tooltip.js?n=29d3032d-3504-4ed1-9d76-46b1a0926e5e"></script>
<script language="javascript" type="text/JavaScript" src="/cposg/js/saj/saj-browser.js?n=3f044b0d-835b-4297-8eee-e3299b9b6a47"></script>
<script language="javascript" type="text/JavaScript" src="/cposg/js/saj/saj-mascara-input.js?n=86cecbf7-9ffb-4489-a73a-f1e57e4cab30"></script>
<script language="javascript" type="text/JavaScript" src="/cposg/js/saj/saj-numeroProcesso.js?n=eef31480-48f5-4c88-b5b4-c680e0035b45"></script>
<script language="javascript" type="text/JavaScript" src="/cposg/js/saj/saj-popup-modal-1.0.0-1.js?n=42a40781-a4e0-46ce-9598-3281f67e3240"></script>
<script language="javascript" type="text/JavaScript" src="/cposg/js/saj/saj-popup.js?n=e0e45e2c-0ce4-47e5-8761-7da51627b034"></script>
<script language="javascript" type="text/JavaScript" src="/cposg/js/spw/spwConcatenado.js?n=6bae810c-1237-4074-8afc-a29daa6cfc99"></script>


<script>
        window.saj = window.saj || {};
        window.saj.env = window.saj.env || {};
        window.saj.env.root = '/cposg';
        window.saj.env.css = '/cposg/css';
        window.saj.env.js = '/cposg/js';
        window.saj.env.imagens = '/cposg/imagens';

        window.saj.cpo = window.saj.cpo || {};
        // transfere variavel se cpo esta rodando para totem
        window.saj.cpo.totem = 'false' == 'true';

        window.saj.cpo.instanciaConsulta = {
                SG5: 'true' == 'true',
                SG5TJ: 'true' == 'true',
                SG5CR: 'false' == 'true',
                value: 'SG5TJ'
        };
</script>

<script language="javascript" type="text/JavaScript" src="/cposg/js/saj-cpo-cbpesquisa.js?n=3431705058"></script>
<script language="javascript" type="text/JavaScript" src="/cposg/js/formulario.js?n=541251654"></script>
<script language="javascript" type="text/JavaScript" src="/cposg/js/saj/acessibilidade/acessibilidade.js?n=719cadbc-3825-44ba-9f46-40a26461164d"></script>





<script>
        (function($){
                $(function(){
                        var intervalo = 1795000;
                        $.saj.manterSessao('/cposg/manterSessao.do', intervalo);
                });

        })(jQuery);
</script>


























<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
<meta http-equiv="pragma" content="no-cache"/>
<meta http-equiv="cache-control" content="no-cache"/>
<meta http-equiv="expires" content="0"/>

<link href="https://esaj.tjsp.jus.br/esaj/tema/padrao/css/esajComum.css" rel="stylesheet" type="text/css" />
<link href="https://esaj.tjsp.jus.br/esaj/tema/padrao/css/esajLayout.css" rel="stylesheet" type="text/css" />
<link href="https://esaj.tjsp.jus.br/esaj/tema/padrao/clientes/SP/css/esajLayoutSP.css" rel="stylesheet" type="text/css" />

<style type="text/css">
<!--
/* botao default means o mais claro, que seria o "botï¿½o principal" */
.spwBotaoDefault, .spwBotaoDefault-o {
        background-image: url(https://esaj.tjsp.jus.br/esaj/tema/padrao/clientes/SP/imagens/layout/fundoBotaoDefault.gif);
}
/* o botao secundario, menos provavel de ser clicado, mais escuro */
.spwBotao, .spwBotao-o {
        background-image: url(https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/fundoBotao.gif);
}
-->
</style>


<script language="javascript" type="text/JavaScript" src="https://esaj.tjsp.jus.br/esaj/tema/padrao/js/menu.js?n=2553626853"></script>

<link rel="shortcut icon" href="https://esaj.tjsp.jus.br/esaj/tema/padrao/clientes/SP/imagens/favicon.ico" type="image/x-icon" />


        <script type="text/javascript">

          var _gaq = _gaq || [];
          _gaq.push(['_setAccount', 'UA-23111004-1']);
          _gaq.push(['_trackPageview']);

          (function() {
            var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
          })();

        </script>






        <!-- Correção temporária do alinhamento do divisor de seção de formulário do SPW -->
        <script type="text/javascript">
                $(function(){$('td[background$="spw/fundo_subtitulo2.gif"]').attr('valign', 'top')});
        </script>
</head>

        <body>









































































                <table width="100%" border="0" cellpadding="0" cellspacing="0" class="esajTabelaCabecalhoCliente" summary=" ">
        <tr>
                <td><a href="http://www.tjsp.jus.br"><img src="https://esaj.tjsp.jus.br/esaj/tema/padrao/clientes/SP/imagens/layout/cabecalhoLogo.jpg" width="425" height="58" alt="Tribunal de Justi&ccedil;a do Estado de S&atilde;o Paulo" /></a></td>
                <td align="right" valign="top"><img src="https://esaj.tjsp.jus.br/esaj/tema/padrao/clientes/SP/imagens/layout/cabecalhoImagem.jpg" width="353" height="58" /></td>
        </tr>
</table>





















<!-- cabecalho e-Saj -->
<table width="100%" cellpadding="0" cellspacing="0" class="esajTabelaCabecalhoServico" summary=" ">
        <tr>
                <td class="esajCelulaCabecalhoServicoLogo">




<a href="https://esaj.tjsp.jus.br/esaj/index.jsp"><img src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/eSajServico.gif" title="Voltar para página inicial do e-SAJ" alt="Voltar para página inicial do e-SAJ" width="255" height="53" border="0" /></a><img src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/eSajServicoInf.gif" alt=" " width="255" height="28" border="0" /></td>
                <td class="esajCelulaCabecalhoServicoMenu">
                    <table width="100%" border="0" cellpadding="0" cellspacing="0" summary=" ">
                                <tr>
                                        <td align="right">











        <div id="divopupContato" style="display: none;">
                <div class="quadroContato"><h2>Suporte Técnico de Sistemas</h2>         <div style="text-align: left; padding: 0 20px;">             <p class="locaisContato">Cadastro de Advogados, Peticionamento Eletrônico e Processos de Primeira Instância Sistemas de 1ª Instância, Sistemas de 2ª Instância, Colégio Recursal, Consulta de Acórdão, Decisões Monocráticas, Homologações de Acordo e Jurisprudência  e Sistema Pushing.</p>             <p class="telefonesLocal"> Ligue para  0800 797 9818 (ligações gratuitas para telefones fixos) ou (11) 4199-6366 (para ligações de celulares) ou abra sua solicitação pelo portal <a target="_blank" href="http://www.suportesistemastjsp.com.br/">www.suportesistemastjsp.com.br</a></p>         </div>     </div>
        </div>


<!-- Devido ao alinhamento inline das imagens, elas não podem ter nenhum tipo de espaçamento entre elas, portanto é necessário finalizar a linha iniciando um comentário e fechar o comentário imediatamente antes da abertura da nova tag-->
<img height="24" width="47" alt=" " src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/inicioMenuSup.jpg"/><a href="https://esaj.tjsp.jus.br/caixapostal"><!--
--><img height="24" width="83" border="0" alt="Caixa postal" src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/caixaPostal.gif"/></a><!--
--><img height="24" width="4" alt=" " src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/menuSeparador.jpg"/><a href="https://esaj.tjsp.jus.br/esaj/cadastro.do"><!--
--><img src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/cadastro.gif" alt="Cadastro" width="81" height="24" border="0" /></a><!--

    --><img height="24" width="4" alt=" " src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/menuSeparador.jpg"/><a id="linkContato" href="#"><!--
    --><img height="24" width="68" border="0" alt="Contato" src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/contato.gif"/></a><!--


    --><img height="24" width="4" alt=" " src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/menuSeparador.jpg"/><a target="blank" href="https://esaj.tjsp.jus.br/WebHelp/"><!--
    --><img height="24" width="61" border="0" alt="Ajuda do e-Saj" src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/ajuda.gif"/></a><!--


--></td>
                                </tr>
                                <tr>
                                        <td class="esajCelulaIdentificacaoServico" >




<style>

    td.esajCelulaIdentificacao, td.esajCelulaIdentificacaoServico {
        position: relative;
    }

    button.escolhaBeta {
        border: solid 1px #aeaeae;
        background: #aeaeae;
        color: #fff;
        margin-right: 5px;
        font-family: verdana;
        font-size: 10px;
        height: 21px;
        text-transform: uppercase;
        line-height: 20px;
        border-radius: 10px;
        text-shadow: 1px 1px 1px #797979;
        position: absolute;
        top: 33px;
        right: 3px;
        padding: 0 19px;

        letter-spacing: 1px;
    }

    button.escolhaBeta:hover {
        background-color: #6c6c6c;
    }

</style>

<span id="identificacao"></span>

<button style="display: none" class="escolhaBeta"></button>






        <script language="javascript" type="text/JavaScript" src="https://esaj.tjsp.jus.br/sajcas/conteudoIdentificacao?script=1558077066606"></script>


</td>
                                </tr>
                                <tr>
                                        <td class="esajCelulaCabecalhoServicoCaminho" >












































<a href="" class="esajCaminhoLink"></a>

 &gt;


<a href="https://esaj.tjsp.jus.br/esaj/portal.do?servico=740000" class="esajCaminhoLink">Bem-vindo</a>

 &gt;


<a href="https://esaj.tjsp.jus.br/esaj/portal.do?servico=190090" class="esajCaminhoLink">Consultas Processuais</a>

 &gt;



Consulta de Processos do 2ºGrau
</td>
                                </tr>
                        </table>
                </td>
        </tr>
</table>
<!-- CONTEUDO -->
<table width="100%" border="0" cellpadding="0" cellspacing="0" class="esajTabelaTitulo">
        <tr>
                <td class="esajCelulaMenuSuspenso">
                <a href="#" onclick="return showMenuSuspenso()"><img src="https://esaj.tjsp.jus.br/esaj/tema/padrao/imagens/layout/menuSuspenso.gif" alt="Menu de servi&ccedil;os" width="243" height="21" style="display:block" /></a>
                <div id="layerMenu" style="display:none">


<!-- MENU -->
<ul id="esajMenuArea">
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Consultas Processuais</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/cpopg/open.do">Consulta de Processos do 1ºGrau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/cposg/open.do">Consulta de Processos do 2ºGrau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/cposgcr/open.do">Colégio Recursal/Turma de Uniformização</a></li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Consulta de Ordem de Processos</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/cop/abrirConsultaDeOrdemDeJulgamentoPg.do">Consulta de processos de Ordem de julgamento do 1º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/cop/abrirConsultaDeOrdemDeAtoPg.do">Consulta de Ordem de Publicação e Cumprimento de Atos</a></li>
</ul>
  </li>
</ul>
  </li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Solicitação de Conciliação</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petpg/abrirSolicitacaoConciliacaoPreProcessual.do">Solicitação de Conciliação Pré-Processual</a></li>
</ul>
  </li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Requisitórios</a>
<ul>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Portal do Devedor</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/cpopg/abrirConsultaDeRequisitorios.do">Consulta de Requisitórios</a></li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Notificação de Requisitórios</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/portalDevedor/abrirConsultaNotificacoesRequisitoriosNaoRecebidas.do">Requisitórios Pendentes de Recebimento</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/portalDevedor/abrirConsultaNotificacoesRequisitoriosRecebidas.do">Requisitórios Recebidos</a></li>
</ul>
  </li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/portalDevedor/abrirConsultaDeProcessos.do">Consulta de Processos</a></li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Notificação de Mapas Orçamentários</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/portalDevedor/abrirConsultaNotificacoesMapasOrcamentariosNaoRecebidas.do">Mapas Pendentes de Recebimento</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/portalDevedor/abrirConsultaNotificacoesMapasOrcamentariosRecebidas.do">Mapas Recebidos</a></li>
</ul>
  </li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/portalDevedor/abrirPeticionamentoIntermediario.do">Peticionamento de Intermediária</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/portalDevedor/abrirConsultaNotificacoesDocumentos.do">Notificação de Documentos</a></li>
</ul>
  </li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/portalDevedor/abrirConsultaListaPagamentos.do">Listas de Precatórios Pendentes de Pagamento e Pagamentos Disponibilizados</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/portalDevedor/abrirConsultaListaDepositos.do">Lista de Depósitos Efetuados</a></li>
</ul>
  </li>
  <li class="esajMenuFechado"><a href="https://esaj.tjsp.jus.br/ctoPtl/abrirConsultaContratos.do">Contratos</a></li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Consultas de Jurisprudência</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/cjsg/consultaSimples.do">Consulta Simples</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/cjsg/consultaCompleta.do">Consulta Completa</a></li>
</ul>
  </li>
  <li class="esajMenuFechado"><a href="https://esaj.tjsp.jus.br/cdje">Diário da Justiça Eletrônico</a></li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Biblioteca</a>
<ul>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Consultas</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/gcnPtl/obrasAbrirConsulta.do">Consulta de Obras, Periódicos e Artigos</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/gcnPtl/jurisprudenciaAbrirConsulta.do">Jurisprudência Selecionada </a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/gcnPtl/legislacaoAbrirConsulta.do">Consulta de Legislação e Normas</a></li>
</ul>
  </li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/gcnPtl/downloadNormasAbrirConsulta.do">Download de Normas</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/gcnPtl/boletimAbrirConsulta.do">Boletins</a></li>
</ul>
  </li>
  <li class="esajMenuFechado"><a href="https://esaj.tjsp.jus.br/push">Push</a></li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Certidões</a>
<ul>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Certidões de 1º Grau</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/sco/abrirCadastro.do">Cadastro de Pedido de Certidão</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/sco/abrirConferencia.do">Conferência de Certidão</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/sco/abrirDownload.do">Visualizar Certidão</a></li>
</ul>
  </li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Certidões de 2º Grau</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/scosg/abrirCadastro.do">Cadastro de Pedido de Certidão de 2º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/scosg/abrirConferencia.do">Conferência de Certidão de 2º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/scosg/abrirDownload.do">Download de Certidão de 2º Grau</a></li>
</ul>
  </li>
</ul>
  </li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Corregedoria</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/cco">Consulta de Pareceres e Decisões da Corregedoria</a></li>
</ul>
  </li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Conferência de Documento Digital</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/pastadigital/pg/abrirConferenciaDocumento.do">Conferência de Documento Digital do 1ºGrau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/pastadigital/sg/abrirConferenciaDocumento.do">Conferência de Documento Digital do 2ºGrau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/pastadigital/sgcr/abrirConferenciaDocumento.do">Conferência de Documento Digital do Colégio Recursal </a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/atendimento/abrirConferenciaDocOriginal.do">Conferência de Documento Digital de Expediente Administrativo </a></li>
</ul>
  </li>
  <li class="esajMenuFechado"><a href="https://esaj.tjsp.jus.br/cjpg">Consulta de Julgados de 1º Grau</a></li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Peticionamento Eletrônico</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petpg/abrirVerificacaoRequisitosPet.do">Verificação de Requisitos</a></li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Peticionamento Eletrônico de 1º Grau</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petpg/abrirNovaPeticaoInicial.do">Petição Inicial de 1° Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petpg/abrirNovaPeticaoIntermediaria.do">Petição Intermediária de 1° Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petpg/abrirConsultaPeticoes.do">Consulta de Petições de 1º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petpg/abrirNovoComplementoProcesso.do">Complemento de Cadastro de 1º Grau</a></li>
</ul>
  </li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Peticionamento Eletrônico de 2º Grau</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petsg/abrirNovaPeticaoInicial.do">Peticionamento Inicial de 2º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petsg/abrirNovaPeticaoIntermediaria.do">Peticionamento Intermediário de 2º Grau</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petsg/abrirConsultaPeticoes.do">Consulta de Petições de 2º Grau</a></li>
</ul>
  </li>
        <li class="esajMenuFechado"><a href="#" onclick="return esajMenu(this)">Peticionamento Eletrônico do Colégio Recursal</a>
<ul>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petcr/abrirNovaPeticaoInicial.do">Peticionamento Inicial - Colégio Recursal</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petcr/abrirNovaPeticaoIntermediaria.do">Peticionamento Intermediário - Colégio Recursal</a></li>
  <li class="esajMenuItem"><a href="https://esaj.tjsp.jus.br/petcr/abrirConsultaPeticoes.do">Consulta de Petições - Colégio Recursal</a></li>
</ul>
  </li>
</ul>
  </li>
</ul>

                </div>
                </td>
                <td class="esajCelulaTituloServico"><h1 class="esajTituloPagina">Consulta de Processos do 2ºGrau</h1></td>
        </tr>
</table>
<table width="100%" cellpadding="0" cellspacing="0" summary=" ">
        <tr>
                <td class="esajCelulaConteudoServico" >









                                        <!-- BEGIN MESSAGE -->
<div id="spwTabelaMensagem">
<table width="100%" height="30" class="tabelaMensagem" border="0" cellpadding="0" cellspacing="0">
  <tr>
        <td width="35" valign="top" class="alert"><img src="/cposg/imagens/spw/icoError.gif" ></td>
        <td class="tituloMensagem"><b>
        Atenção</b></td>  </tr>
  <tr>
       <td class="alert">&nbsp;</td>
       <td tabindex="0" role="alert" id="mensagemRetorno">
           <li>Não foi possível executar esta operação. Tente novamente mais tarde.</li>
       </td>
  </tr>
</table>
<table width="100%" border="0" class="tabelaMensagem" cellpadding="0" cellspacing="0">
  <tr>
       <td width="35">&nbsp;</td>
       <td>&nbsp;
       </td>
  </tr>
</table>
</div>
<!-- END MESSAGE -->

                                        <div style="margin-top: 55px;"></div>































</td>
</tr>
</table>
<table width="100%" border="0" cellpadding="0" cellspacing="0" class="esajTabelaRodape" summary=" ">
    <tr>
        <td class="esajCelulaRodapeCentro">
            Desenvolvido pela Softplan em parceria com a Secretaria de Tecnologia da Informação - STI

        </td>
    </tr>
</table>
<link href="https://esaj.tjsp.jus.br/esaj/tema/padrao/css/saj-popup-modal.css" rel="stylesheet" type="text/css">
<link href="https://esaj.tjsp.jus.br/esaj/tema/padrao/css/popup-beta.css" rel="stylesheet" type="text/css">



<script>
    appEsajLayout = {
        botaoNovaVersao: 'Ir para nova versão',
        botaoVersaoAnterior: 'Ir para versão anterior',
        tituloNovaVersao: 'Nova versão do Portal e-SAJ!',
        tituloVersaoAnterior: 'Versão anterior',
        tituloCertificadoDigital: 'Certificado digital',
        cliente: 'SP',

        emailParaContato: 'esajtjsp@softplan.com.br',
        utilizarBotaoContato: 'true',
        contexto: 'https://esaj.tjsp.jus.br/esaj'
    };
    if(window.jQuery) {
        jQuery.saj = jQuery.saj || {};
        jQuery.saj.certificado = jQuery.saj.certificado || {};
        jQuery.saj.certificado.cliente = 'SP';
        jQuery.saj.certificado.tituloCertificadoDigital = 'Certificado digital';
        jQuery.saj.certificado.tituloProblemasAoAssinar = 'Falha de comunicação com o dispositivo de assinatura digital';
        jQuery.saj.certificado.urlConteudoAjudaWebSigner = appEsajLayout.contexto + '/ajudaWebSigner.do';
        jQuery.saj.certificado.licenca = 'ARkEKi50anNwLmp1cy5iciwxMC4zMy4xOTIuMTAxLDEwLjMzLjE5Mi4xMDUsMTAuMzMuMTkyLjE0NiwxMC4zMy4xOTIuMjQxLDEwLjMzLjE5Mi45MCwxMC4zMy4xOTIuOTEsMTAuMzMuMTkyLjkyLDEwLjMzLjE5Mi45NCwxMC4zMy4xOTMuMTg1LDEwLjMzLjE5My4xODYsMTAuMzMuMTkzLjE4NywxMC4zMy4xOTMuMTg4LDEwLjMzLjE5NC4yMjQsMTAuMzMuMTk0LjIyNSwxMC4zMy4xOTQuMjU1LDEwLjMzLjE5NC43NCwxMC4zMy4xOTQuNzUsMTAuMzMuMTk0Ljc2LDEwLjMzLjE5NC43NywxMC4zMy4xOTQuNzksMTAuMzMuMTk1LjEwMiwxMC4zMy4xOTUuMTAyLDEwLjMzLjE5NS4xMTksMTAuMzMuMTk1LjEyMSwxMC4zMy4xOTUuMTIyLDEwLjMzLjE5NS4xMjMsMTAuMzMuMTk1LjEyNCwxMC4zMy4xOTUuMTI1LDEwLjMzLjE5NS4xMjYsMTAuMzMuMTk1LjEyNywxMC4zMy4xOTUuMTI4LDEwLjMzLjE5NS4xMjksMTAuMzMuMTk1LjEzMCwxMC4zMy4xOTUuMTMxLDEwLjMzLjE5NS4xMzIsMTAuMzMuMTk1LjE4MywxMC4zMy4xOTUuMTg0LDEwLjMzLjE5NS4xODUsMTAuMzMuMTk1LjE4NiwxMC4zMy4xOTUuMTg3LDEwLjMzLjE5NS4xODgsMTAuMzMuMTk1LjE4OSwxMC4zMy4xOTUuMTkxLDEwLjMzLjE5NS4xOTIsMTAuMzMuMTk1LjE5MywxMC4zMy4xOTUuMTk0LDEwLjMzLjE5NS4xOTUsMTAuMzMuMTk1LjE5NSwxMC4zMy4xOTUuMTk3LDEwLjMzLjE5NS4xOTgsMTAuMzMuMTk1LjIzNCwxMC4zMy4xOTUuMjM3LDEwLjk4LjE5Mi4xMTMsMTAuOTguMTkyLjExNCwxMC45OC4xOTIuMTE3LDEwLjk4LjE5Mi4yNTAsMTAuOTguMTkyLjQyLDEwLjk4LjE5Mi43MCwxMC45OC4xOTIuNzEsMTAuOTguMTkzLjEyMSwxMC45OC4xOTMuMTIyLDEwLjk4LjE5My4xOTksMTAuOTguMTkzLjIwMCwxMC45OC4xOTMuMjAxLDEwLjk4LjE5My4yMDIsMTAuOTguMTkzLjIyNSwxMC45OC4xOTQuMTIxLDEwLjk4LjE5NC4xMjIsMTAuOTguMTk0LjE0MSwxMC45OC4xOTQuMTQyLDEwLjk4LjE5NC4xNDMsMTAuOTguMTk0LjE0NCwxMC45OC4xOTQuMTQ1LDEwLjk4LjE5NC4xNDcsMTAuOTguMzIuNzYAAAABt8T6Ov8g0lWHnOe7bekYQC1kjn/SgVPWGteqlpMDF8qEOKOxdWahBlk0uh9nfmPiUY9MXcXchlgu6V/zygYGgSfZG11odlUkrXZCAYX/pB3ArsqmrqgvMK0mxuTVOThs/flGWltXnCFEFEU1Pp6RSdlhtCOEuGx5XWov3lux8DcnB+DxL2zauU4GfGJmoXCZDMWT2g7MXIu7VjrJJEkCH/nZ0hkhUsw/k0ORu7/kXJyBufrFZYbsQ/Nadjp9CgYhlsjKXmSPSn8GU8xUetHXGX3FzFJriyk8iqcH72p4z0/Msif4S+VNz0JV3+xffRvdmKuG28jHHDUqBxIrhjs+XA==';
        jQuery.saj.certificado.cofreDigital = jQuery.saj.certificado.cofreDigital || {};
        jQuery.saj.certificado.cofreDigital.habilitado = 'false' === 'true';
        jQuery.saj.certificado.cofreDigital.enderecoBase = 'https://esaj.tjsp.jus.br/esaj';
    }

</script>
<script src="https://esaj.tjsp.jus.br/esaj/js/app-bundle.js?n=2830363862"></script>
<script language="javascript" type="text/JavaScript" src="https://websigner.softplan.com.br/Content/js/softplan-websigner-2.5.0.js?n=62fddc48-c657-4f9b-95db-73bb59e7bb4b"></script>

<script language="javascript" type="text/JavaScript" src="https://esaj.tjsp.jus.br/esaj/js/saj-certificado.js?n=2205257179"></script>



<div id="webSignerNaoInstalado" style="display: none;">
    <p>Para utilização do certificado digital no Portal e-SAJ é necessário a instalação do plug-in Web Signer. Por favor, realize a instalação antes de continuar.</p>
    <div class="footer_certificado">
        <button id="redirecionarParaPaginaInstalacao" class="actionPrincipal spwBotaoDefault">Instalar</button>
        <button class="fecharModalInstalacao spwBotao">Cancelar</button>
        <button class="spwBotao" onclick="window.open('https://esaj.tjsp.jus.br/WebHelp//#id_instalacao_lacuna.htm','_blank')">Ajuda</button>
    </div>
</div>

<div id="webSignerNaoSuportado" style="display: none;">
    <p>O navegador utilizado não é compatível com a tecnologia (Web Signer) necessária para utilização do certificado digital. Por favor, utilize um dos navegadores homologados. Em caso de dúvidas, efetue a validação de requisitos <a href="https://esaj.tjsp.jus.br/petpg/abrirVerificacaoRequisitosPet.do" target="_blank">aqui</a>.</p>
    <div class="footer_certificado">
        <button class="fecharModalInstalacao spwBotaoDefault actionPrincipal">OK</button>
    </div>
</div>














                <!-- CAUSA: Exceção: java.lang.NullPointerException -->

<script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"errorBeacon":"bam.nr-data.net","licenseKey":"b61bdf610d","agent":"","beacon":"bam.nr-data.net","applicationTime":27,"applicationID":"34412805","transactionName":"MlZRN0QECkMAVERZDgscYBdEEBBDIFREWQ4LHFERGAYLXU9EX1YVFV9SDRgWBVpPVEBfEgIdQBdEEBBDT1ZTRAgKXR0wXgoTcQJDWV8P","queueTime":0}</script></body>

</html>

"""
