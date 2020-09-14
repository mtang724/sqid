"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
exports.__esModule = true;
var vue_1 = require("vue");
var vue_router_1 = require("vue-router");
var Home_vue_1 = require("@/views/Home.vue");
var progress_1 = require("./progress");
var index_1 = require("@/store/index");
var types_1 = require("@/api/types");
var wikidata_1 = require("@/api/wikidata");
vue_1["default"].use(vue_router_1["default"]);
var ensureEntityIsValid = function (to, _from, next) { return __awaiter(void 0, void 0, void 0, function () {
    var entityId, err_1;
    return __generator(this, function (_a) {
        switch (_a.label) {
            case 0:
                entityId = to.params.id;
                if (entityId === undefined) {
                    return [2 /*return*/, next({ name: 'not-found' })];
                }
                _a.label = 1;
            case 1:
                _a.trys.push([1, 3, , 4]);
                return [4 /*yield*/, wikidata_1.getEntityInfo(entityId)];
            case 2:
                _a.sent();
                return [3 /*break*/, 4];
            case 3:
                err_1 = _a.sent();
                if (err_1 instanceof types_1.MalformedEntityIdError) {
                    return [2 /*return*/, next({ name: 'invalid-entity',
                            params: { id: err_1.entityId }
                        })];
                }
                if (err_1 instanceof types_1.EntityMissingError) {
                    return [2 /*return*/, next({ name: 'not-found',
                            params: { id: err_1.entityId }
                        })];
                }
                return [2 /*return*/, next(err_1)];
            case 4: return [2 /*return*/, next()];
        }
    });
}); };
var ensureEntityIsInvalid = function (to, _from, next) { return __awaiter(void 0, void 0, void 0, function () {
    var entityId, err_2;
    return __generator(this, function (_a) {
        switch (_a.label) {
            case 0:
                entityId = to.params.id;
                if (entityId === undefined) {
                    return [2 /*return*/, next()];
                }
                _a.label = 1;
            case 1:
                _a.trys.push([1, 3, , 4]);
                return [4 /*yield*/, wikidata_1.getEntityInfo(entityId)];
            case 2:
                _a.sent();
                return [3 /*break*/, 4];
            case 3:
                err_2 = _a.sent();
                if (err_2 instanceof types_1.MalformedEntityIdError ||
                    err_2 instanceof types_1.EntityMissingError) {
                    return [2 /*return*/, next()];
                }
                return [2 /*return*/, next(err_2)];
            case 4: 
            // actually a valid entity, redirect
            return [2 /*return*/, next({ name: 'entity',
                    params: { id: entityId }
                })];
        }
    });
}); };
var router = new vue_router_1["default"]({
    mode: 'history',
    // mode: "hash",
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home_vue_1["default"],
            meta: { title: 'SQID – Wikidata Explorer' }
        },
        {
            path: '/about',
            name: 'about',
            // route level code-splitting
            // this generates a separate chunk (about.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: function () { return Promise.resolve().then(function () { return require(/* webpackChunkName: "about" */ '@/views/About.vue'); }); },
            meta: { title: 'SQID – About' }
        },
        {
            path: '/status',
            name: 'status',
            component: function () { return Promise.resolve().then(function () { return require(/* webpackChunkName: "status" */ '@/views/Status.vue'); }); },
            meta: { title: 'SQID – Status' }
        },
        {
            path: '/entity/:id',
            name: 'entity',
            component: function () { return Promise.resolve().then(function () { return require(/* webpackChunkName: "entity" */ '@/views/Entity.vue'); }); },
            props: true,
            beforeEnter: ensureEntityIsValid
        },
        {
            path: '/classes/',
            name: 'classes',
            component: function () { return Promise.resolve().then(function () { return require(/* webpackChunkName: "construction" */ '@/views/Construction.vue'); }); }
        },
        {
            path: '/properties/',
            name: 'properties',
            component: function () { return Promise.resolve().then(function () { return require(/* webpackChunkName: "construction" */ '@/views/Construction.vue'); }); }
        },
        {
            path: '/rules/',
            name: 'rules',
            component: function () { return Promise.resolve().then(function () { return require(/* webpackChunkName: "construction" */ '@/views/Construction.vue'); }); }
        },
        {
            path: '/lexemes/',
            name: 'lexemes',
            component: function () { return Promise.resolve().then(function () { return require(/* webpackChunkName: "construction" */ '@/views/Construction.vue'); }); }
        },
        {
            path: '/invalid/:id',
            name: 'invalid-entity',
            component: function () { return Promise.resolve().then(function () { return require(/* webpackChunkName: "invalidEntity" */ '@/views/InvalidEntity.vue'); }); },
            props: true,
            beforeEnter: ensureEntityIsInvalid
        },
        {
            path: '/404/:id?',
            name: 'not-found',
            component: function () { return Promise.resolve().then(function () { return require(/* webpackChunkName: "notFound" */ '@/views/NotFound.vue'); }); },
            props: true,
            beforeEnter: ensureEntityIsInvalid
        },
        {
            path: '*',
            redirect: { name: 'not-found' }
        },
    ]
});
router.beforeResolve(function (_to, _from, next) {
    progress_1["default"].start();
    next();
});
router.beforeEach(function (to, _from, next) { return __awaiter(void 0, void 0, void 0, function () {
    var query, lang;
    return __generator(this, function (_a) {
        query = to.query;
        if (query && 'lang' in query) {
            lang = query.lang.toString();
            index_1["default"].commit('setTranslationFromUri');
            index_1["default"].dispatch('loadTranslation', lang);
        }
        next();
        return [2 /*return*/];
    });
}); });
router.beforeEach(function (to, _from, next) { return __awaiter(void 0, void 0, void 0, function () {
    var query, verifier, key;
    return __generator(this, function (_a) {
        query = to.query;
        if (query && 'oauth_verifier' in query && 'oauth_token' in query) {
            verifier = query.oauth_verifier.toString();
            key = query.oauth_token.toString();
            index_1["default"].dispatch('complete', { verifier: verifier, key: key });
        }
        next();
        return [2 /*return*/];
    });
}); });
router.beforeEach(function (to, _from, next) {
    var segments = to.matched.slice().reverse();
    var title = segments.find(function (segment) { return segment.meta && segment.meta.title; });
    if (title) {
        document.title = title.meta.title;
    }
    next();
});
router.afterEach(function (_to, _from) { return progress_1["default"].done(); });
exports["default"] = router;
