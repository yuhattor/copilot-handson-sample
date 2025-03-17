# -*- mode: ruby -*-
# vi: set ft=ruby :

###
### 問い合わせのデータテーブル作成
###

create_table "inquiries", id: { type: :string, limit: 36, comment: "Primary Key" }, force: :cascade do |t|
  t.string "user_id", :limit => 36
  t.string "listing_id", :limit => 36
  t.text "message"
  t.datetime "discarded_at"
  t.datetime "created_at", precision: 6, null: false
  t.datetime "updated_at", precision: 6, null: false
  t.index ["discarded_at"], name: "index_inquiries_on_discarded_at"
  t.index ["user_id"], name: "index_inquiries_on_user_id"
  t.index ["user_id"], name: "index_reservations_on_user_id"
end



###
### 予約のデータテーブル作成
###

create_table "reservations", id: { type: :string, limit: 36, comment: "Primary Key" }, force: :cascade do |t|
  t.string "user_id", :limit => 36
  t.string "listing_id", :limit => 36
  t.datetime "appointment"
  t.datetime "discarded_at"
  t.datetime "created_at", precision: 6, null: false
  t.datetime "updated_at", precision: 6, null: false
  t.index ["discarded_at"], name: "index_reservations_on_discarded_at"
  t.index ["user_id"], name: "index_reservations_on_user_id"
end

###
### ユーザーのデータテーブル
###

create_table "users", id: { type: :string, limit: 36, comment: "Primary Key" }, force: :cascade do |t|

  ### プロフィール関連
  t.string "first_name"
  t.string "last_name"
  t.string "first_name_kana"
  t.string "last_name_kana"
  t.date "birthday"
  t.string "gender"
  t.string "uid", :limit => 36
  t.string "email"
  t.boolean "email_verified"
  t.string "phone_number"
  t.string "picture"

  ### 住所関連
  t.string "zipcode"
  t.string "prefecture"
  t.string "city"
  t.string "town"
  t.string "address1"
  t.string "address2"
  t.string "building_name"
  
  ### 組織など
  t.string "organization"
  t.string "industry"
  t.string "occupation"
  t.string "employment_type"
  t.integer "service_years"
  t.integer "annual_income"

  ### ローンと予算関連
  t.float "estimated_interest_rate"
  t.integer "down_payment"
  t.integer "budget"
  t.integer "household_income"
  t.integer "anual_income"
  t.integer "own_capital"
  t.integer "liabilities"
  t.integer "loan_repayment_period"

  ### 家族構成など
  t.integer "family_structure"
  t.integer "dependents"
  t.boolean "marriage"
  t.boolean "has_spouse"

  t.datetime "discarded_at"
  t.datetime "created_at", precision: 6, null: false
  t.datetime "updated_at", precision: 6, null: false
  t.index ["discarded_at"], name: "index_users_on_discarded_at"
  t.index ["uid"], name: "index_users_on_uid", unique: true
end


###
### フィルターのデータテーブル
###

create_table "filters", id: { type: :string, limit: 36, comment: "Primary Key" }, force: :cascade do |t|
  t.string "user_id", :limit => 36
  t.string "name"
  t.string "description"
  t.string "text"
  t.string "code"
  t.string "sort"
  t.string "sort_by"
  t.string "handover"
  t.string "parking_lot_availability"
  t.string "share" #To be enum
  t.integer "min_price"
  t.integer "max_price"
  t.integer "min_age"
  t.integer "max_age"
  t.integer "min_area"
  t.integer "max_area"
  t.string "land_rights"
  t.json "floorplans"
  t.json "directions"
  t.json "facilities"
  t.datetime "discarded_at"
  t.datetime "created_at", precision: 6, null: false
  t.datetime "updated_at", precision: 6, null: false
  t.index ["discarded_at"], name: "index_filters_on_discarded_at"
  t.index ["user_id"], name: "index_filters_on_user_id"
end


###
### Favorite のデータテーブル
###

create_table "favorites", id: { type: :string, limit: 36, comment: "Primary Key" }, force: :cascade do |t|
  t.string "user_id", :limit => 36
  t.string "share"
  t.string "title"
  t.string "description"
  t.json "listings", :default=> '[]'
  t.datetime "discarded_at"
  t.datetime "created_at", precision: 6, null: false
  t.datetime "updated_at", precision: 6, null: false
  t.index ["discarded_at"], name: "index_favorites_on_discarded_at"
  t.index ["user_id"], name: "index_favorites_on_user_id"
end


###
### Invitation のデータテーブル
###

create_table "invitations", id: { type: :string, limit: 36, comment: "Primary Key" }, force: :cascade do |t|
  t.string "user_id", :limit => 36
  t.string "email"
  t.datetime "invited_at"
  t.datetime "canceled_at"
  t.datetime "activated_at"
  t.string "activated_by", :limit => 36
  t.datetime "discarded_at"
  t.datetime "created_at", precision: 6, null: false
  t.datetime "updated_at", precision: 6, null: false
  t.index ["discarded_at"], name: "index_invitations_on_discarded_at"
  t.index ["user_id"], name: "index_invitations_on_user_id"
  t.index ["activated_by"], name: "index_invitations_on_activated_by"
end

add_foreign_key "invitations", "users"
add_foreign_key "inquiries", "users"
add_foreign_key "filters", "users"
add_foreign_key "reservations", "users"