CREATE TABLE documents (
    document_id VARCHAR(63) PRIMARY KEY, -- Primary key, unique ID
    store_facility VARCHAR(63) NOT NULL, -- Storage facility (name of the SST where actual data exists)
    sst_document_id VARCHAR(63) NOT NULL, -- Communication document ID
    title VARCHAR(255) NOT NULL, -- Title
    from_adr TEXT NOT NULL, -- Sender's address
    to_adr TEXT NOT NULL, -- Recipient's address
    data_type VARCHAR(63) NOT NULL, -- Content data type
    extra_data TEXT, -- Additional data type
    pt_guid VARCHAR(255), -- Patient guide in case of a patient
    password_text VARCHAR(63), -- Security password
    create_date TIMESTAMP WITHOUT TIME ZONE NOT NULL, -- Creation date
    last_status VARCHAR(63), -- Last status
    last_caption VARCHAR(255), -- Last description
    last_update TIMESTAMP WITHOUT TIME ZONE, -- Last update date
    limit_date TIMESTAMP WITHOUT TIME ZONE, -- Expiry date
    fix_flg VARCHAR(1), -- Fixed flag (0: normal, 1: fixed)
    del_flg VARCHAR(1) -- Delete flag (1: deleted, 0: valid)
);
