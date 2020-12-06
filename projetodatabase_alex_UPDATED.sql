PGDMP                         x            projeto    13.0    13.0     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    32779    projeto    DATABASE     k   CREATE DATABASE projeto WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE projeto;
                postgres    false            �            1259    32786    movies    TABLE     (  CREATE TABLE public.movies (
    itemid integer NOT NULL,
    name character varying,
    actorid integer NOT NULL,
    director character varying,
    imdbrating double precision,
    genre character varying,
    price double precision,
    year bigint,
    timeavaible bigint,
    type text
);
    DROP TABLE public.movies;
       public         heap    postgres    false            �            1259    32798    movies_actorid_seq    SEQUENCE     �   CREATE SEQUENCE public.movies_actorid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.movies_actorid_seq;
       public          postgres    false    201            �           0    0    movies_actorid_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.movies_actorid_seq OWNED BY public.movies.actorid;
          public          postgres    false    203            �            1259    32789    movies_itemid_seq    SEQUENCE     �   CREATE SEQUENCE public.movies_itemid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.movies_itemid_seq;
       public          postgres    false    201            �           0    0    movies_itemid_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.movies_itemid_seq OWNED BY public.movies.itemid;
          public          postgres    false    202            �            1259    32807    rent    TABLE     �   CREATE TABLE public.rent (
    clientid bigint,
    date timestamp without time zone,
    price real,
    dateend timestamp without time zone,
    usermail text,
    timeavaible bigint,
    orderid integer NOT NULL,
    type text,
    movieid bigint
);
    DROP TABLE public.rent;
       public         heap    postgres    false            �            1259    41008    rent_orderid_seq    SEQUENCE     �   CREATE SEQUENCE public.rent_orderid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.rent_orderid_seq;
       public          postgres    false    204            �           0    0    rent_orderid_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.rent_orderid_seq OWNED BY public.rent.orderid;
          public          postgres    false    205            �            1259    32780    users    TABLE     �   CREATE TABLE public.users (
    nome text,
    email text,
    password text,
    balance double precision,
    userid integer NOT NULL
);
    DROP TABLE public.users;
       public         heap    postgres    false            �            1259    41020    users_userid_seq    SEQUENCE     �   CREATE SEQUENCE public.users_userid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.users_userid_seq;
       public          postgres    false    200            �           0    0    users_userid_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.users_userid_seq OWNED BY public.users.userid;
          public          postgres    false    206            4           2604    32791    movies itemid    DEFAULT     n   ALTER TABLE ONLY public.movies ALTER COLUMN itemid SET DEFAULT nextval('public.movies_itemid_seq'::regclass);
 <   ALTER TABLE public.movies ALTER COLUMN itemid DROP DEFAULT;
       public          postgres    false    202    201            5           2604    32800    movies actorid    DEFAULT     p   ALTER TABLE ONLY public.movies ALTER COLUMN actorid SET DEFAULT nextval('public.movies_actorid_seq'::regclass);
 =   ALTER TABLE public.movies ALTER COLUMN actorid DROP DEFAULT;
       public          postgres    false    203    201            6           2604    41010    rent orderid    DEFAULT     l   ALTER TABLE ONLY public.rent ALTER COLUMN orderid SET DEFAULT nextval('public.rent_orderid_seq'::regclass);
 ;   ALTER TABLE public.rent ALTER COLUMN orderid DROP DEFAULT;
       public          postgres    false    205    204            3           2604    41022    users userid    DEFAULT     l   ALTER TABLE ONLY public.users ALTER COLUMN userid SET DEFAULT nextval('public.users_userid_seq'::regclass);
 ;   ALTER TABLE public.users ALTER COLUMN userid DROP DEFAULT;
       public          postgres    false    206    200            �          0    32786    movies 
   TABLE DATA           t   COPY public.movies (itemid, name, actorid, director, imdbrating, genre, price, year, timeavaible, type) FROM stdin;
    public          postgres    false    201   �       �          0    32807    rent 
   TABLE DATA           m   COPY public.rent (clientid, date, price, dateend, usermail, timeavaible, orderid, type, movieid) FROM stdin;
    public          postgres    false    204   l       �          0    32780    users 
   TABLE DATA           G   COPY public.users (nome, email, password, balance, userid) FROM stdin;
    public          postgres    false    200          �           0    0    movies_actorid_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.movies_actorid_seq', 1, false);
          public          postgres    false    203            �           0    0    movies_itemid_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.movies_itemid_seq', 1, false);
          public          postgres    false    202            �           0    0    rent_orderid_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.rent_orderid_seq', 37, true);
          public          postgres    false    205            �           0    0    users_userid_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.users_userid_seq', 2, true);
          public          postgres    false    206            :           2606    41012    rent rent_orderid_key 
   CONSTRAINT     S   ALTER TABLE ONLY public.rent
    ADD CONSTRAINT rent_orderid_key UNIQUE (orderid);
 ?   ALTER TABLE ONLY public.rent DROP CONSTRAINT rent_orderid_key;
       public            postgres    false    204            8           2606    41024    users users_userid_key 
   CONSTRAINT     S   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_userid_key UNIQUE (userid);
 @   ALTER TABLE ONLY public.users DROP CONSTRAINT users_userid_key;
       public            postgres    false    200            �   �   x�M�A�0��p���Т`�]�������G�淢�%.g2/�؉���'���QÀ:�L��xJ�������}�g%�ΫCpWJ����j�p'��`+�{�Yk[�E��Л�Nx��
G�ă:]�D=6�5�YV��J���Vȵ,�_WkT_rγ,� z B�      �   �   x�m�1�0D�z}�\��ά��>E
$��(V"P��=
���uZF+L�
�'�u@��p{,�X���}_��G�M51Wz���su�l�AJ��
����7,w���	ވFMf%���<*έC�!\S��S?w      �   )   x��� BC=CNC�Ĝ�
Naij�g`�i����� �	�     